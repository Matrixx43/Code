repeat_exp = 1000;
repeat_toss = 100;

heads = 0;
n_heads = [];

for i = 1:repeat_exp
  heads = 0;
  for j = 1:repeat_toss
    if randi(2) == 1
      heads++;
    endif
  endfor
  n_heads = [n_heads, heads];
endfor

hist(n_heads, 20);

