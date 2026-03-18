# 式変形典型

$$(1+ax^r)^n = \sum_{i=0}^\infty \binom{n}{i}a^i x^{ir}$$

### 特に

$$
\begin{aligned}
\frac{1}{(1+ax^r)^n} &= (1+ax^r)^{-n} \\
&= \sum_{i=0}^\infty \binom{-n}{i}a^i x^{ir}\\
&= \sum_{i=0}^\infty (-1)^i\binom{i+n-1}{i} a^ix^{ir}
\end{aligned}
$$

# 指数型母関数
$$
R(x)=\sum_{i=0}^{\infty}\frac{x^i}{i!}=e^x \\
\left[\frac{x^n}{n!}\right]e^{ax}=a^n
$$

# 偶数,奇数
$$
A(x)=\sum_{i=0}^{\infty}a_ix^i \\
$$
について
$$
\frac{A(x)+A(-x)}{2}=\sum_{i\geq 0,i:偶数}a_ix^i \\
\frac{A(x)-A(-x)}{2}=\sum_{i\geq 0,i:奇数}a_ix^i
$$
