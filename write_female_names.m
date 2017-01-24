inputs_cell = cell(1,1);
% choose a random number to initiate the input
r = randi([1 28],1,1);

in = zeros(1,28);
in(r) = 1;

inputs_cell{1} = in;

for char = 1:70
    for i = 1:size(inputs_cell,2)

        % set the initial activations
        a = inputs_cell{i}';

        % pass to hidden layer
        z = u_weights_cell{i}*a + hidden_bias_cell{i};

        if i > 1 % add the weighted input from the hidden nodes in the previous step
            z_w = w_weights_cell{i}*hidden_activation_cell{i-1};
            z = z + z_w;
        end

        % compute activation for the hidden layer
        a = logsig(z);
        hidden_activation_cell{i} = a;          

        % compute the activation for the output layer (v weights)
        z = v_weights_cell{i}*hidden_activation_cell{i} + output_bias_cell{i};

        a = logsig(z);

    end

    [val idx] = max(a);

    next_output = zeros(1,size(a,1));
    next_output(idx) = 1;
    inputs_cell(end+1) = {[next_output]};
end


fileID = fopen('C:\\Ross\\female_chars_output.txt','w');
formatSpec = '%i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i %i\n';
for j = 1:char
    fprintf(fileID,formatSpec,inputs_cell{j});
end
fclose(fileID);

