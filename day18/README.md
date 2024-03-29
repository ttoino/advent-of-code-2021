# Day 18: Snailfish

You descend into the ocean trench and encounter some [snailfish](https://en.wikipedia.org/wiki/Snailfish). They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his **math homework**.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a **pair** - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as `[x,y]`, where `x` and `y` are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

```
[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
```

This snailfish homework is about **addition**. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, `[1,2]` + `[[3,4],5]` becomes `[[1,2],[[3,4],5]]`.

There's only one problem: **snailfish numbers must always be reduced**, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To **reduce a snailfish number**, you must repeatedly do the first action in this list that applies to the snailfish number:

- If any pair is **nested inside four pairs**, the leftmost such pair **explodes**.
- If any regular number is **10 or greater**, the leftmost such regular number **splits**.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if **split** produces a pair that meets the **explode** criteria, that pair **explodes** before other **splits** occur.

To **explode** a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number `0`.

Here are some examples of a single explode action:

- <code>[[[[<strong>[9,8]</strong>,1],2],3],4]</code> becomes <code>[[[[<strong>0</strong>,<strong>9</strong>],2],3],4]</code> (the `9` has no regular number to its left, so it is not added to any regular number).
- <code>[7,[6,[5,[4,<strong>[3,2]</strong>]]]]</code> becomes <code>[7,[6,[5,[<strong>7</strong>,<strong>0</strong>]]]]</code> (the `2` has no regular number to its right, and so it is not added to any regular number).
- <code>[[6,[5,[4,<strong>[3,2]</strong>]]],1]</code> becomes <code>[[6,[5,[<strong>7</strong>,<strong>0</strong>]]],<strong>3</strong>]</code>.
- <code>[[3,[2,[1,<strong>[7,3]</strong>]]],[6,[5,[4,[3,2]]]]]</code> becomes <code>[[3,[2,[<strong>8</strong>,<strong>0</strong>]]],[<strong>9</strong>,[5,[4,[3,2]]]]]</code> (the pair `[3,2]` is unaffected because the pair `[7,3]` is further to the left; `[3,2]` would explode on the next action).
- <code>[[3,[2,[8,0]]],[9,[5,[4,<strong>[3,2]</strong>]]]]</code> becomes <code>[[3,[2,[8,0]]],[9,[5,[<strong>7</strong>,<strong>0</strong>]]]]</code>.

To **split** a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded **down**, while the right element of the pair should be the regular number divided by two and rounded **up**. For example, `10` becomes `[5,5]`, `11` becomes `[5,6]`, `12` becomes `[6,6]`, and so on.

Here is the process of finding the reduced result of `[[[[4,3],4],4],[7,[[8,4],9]]]` + `[1,1]`:

<pre><code>after addition: [[[[<strong>[4,3]</strong>,4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[<strong>[8,4]</strong>,9]]],[1,1]]
after explode:  [[[[0,7],4],[<strong>15</strong>,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,<strong>13</strong>]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,<strong>[6,7]</strong>]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
</code></pre>

Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]`.

The homework assignment involves adding up a **list of snailfish numbers** (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is `[[[[1,1],[2,2]],[3,3]],[4,4]]`:

```
[1,1]
[2,2]
[3,3]
[4,4]
```

The final sum of this list is `[[[[3,0],[5,3]],[4,4]],[5,5]]`:

```
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
```

The final sum of this list is `[[[[5,0],[7,4]],[5,5]],[6,6]]`:

```
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
```

Here's a slightly larger example:

```
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
```

The final sum `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` is found after adding up the above snailfish numbers:

```
  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
```

To check whether it's the right answer, the snailfish teacher only checks the **magnitude** of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of `[9,1]` is <code>3\*9 + 2\*1 = <strong>29</strong></code>; the magnitude of `[1,9]` is <code>3\*1 + 2\*9 = <strong>21</strong></code>. Magnitude calculations are recursive: the magnitude of `[[9,1],[1,9]]` is <code>3\*29 + 2\*21 = <strong>129</strong></code>.

Here are a few more magnitude examples:

- `[[1,2],[[3,4],5]]` becomes **`143`**.
- `[[[[0,7],4],[[7,8],[6,0]]],[8,1]]` becomes **`1384`**.
- `[[[[1,1],[2,2]],[3,3]],[4,4]]` becomes **`445`**.
- `[[[[3,0],[5,3]],[4,4]],[5,5]]` becomes **`791`**.
- `[[[[5,0],[7,4]],[5,5]],[6,6]]` becomes **`1137`**.
- `[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]` becomes **`3488`**.

So, given this example homework assignment:

```
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
```

The final sum is:

```
[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
```

The magnitude of this final sum is **`4140`**.

Add up all of the snailfish numbers from the homework assignment in the order they appear. **What is the magnitude of the final sum?**
