m_size = 10;

matrix = zeros(m_size,m_size - 1);
matrix = [ones(m_size,1), matrix];

for i = 2:m_size
  for j = 2:(m_size - 1)
    matrix(i, j) = matrix(i - 1, j - 1) + matrix(i - 1, j);
  endfor
endfor

disp(matrix)