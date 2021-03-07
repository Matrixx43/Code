function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

[vert, hoz] = size(g);
for i = 1:vert
  for j = 1:hoz
    g(i, j) = 1/(1 + 1/exp(z(i,j)));
  endfor
endfor



% =============================================================

end
