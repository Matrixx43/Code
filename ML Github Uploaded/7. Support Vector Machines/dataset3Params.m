function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

% Values to try
values = [0 0.01 0.03 0.1 0.3 1 3 10 30]';
nvalues = length(values);

% Errors matrix to fill
errors = zeros(nvalues);

% Loop over c and sigma
for i = 1:nvalues
  % Declare C_test
  C_test = values(i);
  for j = 1:nvalues
    % Declare sigma_test
    sigma_test = values(j);
    % Compute the error
    model= svmTrain(X, y, C_test, @(x1, x2) gaussianKernel(x1, x2, sigma_test));
    predictions = svmPredict(model, Xval);
    errors(i, j) = mean(double(predictions ~= yval));
  endfor
endfor

% Select lowest values
[x, j] = min(min(errors));
[x, i] = min(min(errors'));
C = values(i);
sigma = values(j);







% =========================================================================

end
