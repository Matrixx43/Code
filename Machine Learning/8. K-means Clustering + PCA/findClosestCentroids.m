function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%

% Set m
m = size(X, 1);

% Iterate over training samples
for i = 1:m
  minidx = 1;
  mind = sum((X(i:i,:) - centroids(1:1,:)).^2);
  % Iterate over the centroids to find closest one
  for k = 2:K
    % Compute the distance
    d = sum((X(i:i,:) - centroids(k:k,:)).^2);
    % If it is smaller
    if d <= mind
      minidx = k;
      mind = d;
    endif
  endfor
  % Assign the index of closest centroid
  idx(i) = minidx;
endfor





% =============================================================

end

