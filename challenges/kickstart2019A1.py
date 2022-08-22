'''
Google kickstart 2019 Round A -> Training 
--------------
Problem
As the football coach at your local school, you have been tasked with picking a team of exactly P students to represent your school. There are N students for you to pick from. The i-th student has a skill rating Si, which is a positive integer indicating how skilled they are.
You have decided that a team is fair if it has exactly P students on it and they all have the same skill rating. That way, everyone plays as a team. Initially, it might not be possible to pick a fair team, so you will give some of the students one-on-one coaching. It takes one hour of coaching to increase the skill rating of any student by 1.
The competition season is starting very soon (in fact, the first match has already started!), so you'd like to find the minimum number of hours of coaching you need to give before you are able to pick a fair team.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing the two integers N and P, the number of students and the number of students you need to pick, respectively. Then, another line follows containing N integers Si; the i-th of these is the skill of the i-th student.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of hours of coaching needed, before you can pick a fair team of P students.

Limits
Time limit: 15 seconds per test set.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
1 ≤ Si ≤ 10000, for all i.
2 ≤ P ≤ N.
Test set 1 (Visible)
2 ≤ N ≤ 1000.

Test set 2 (Hidden)
2 ≤ N ≤ 105.

Sample
Sample Input
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7
Sample Output
Case #1: 14
Case #2: 0
Case #3: 6
In Sample Case #1, you can spend a total of 6 hours training the first student and 8 hours training the second one. This gives the first, second and third students a skill level of 9. This is the minimum time you can spend, so the answer is 14.

In Sample Case #2, you can already pick a fair team (the first and second student) without having to do any coaching, so the answer is 0.

In Sample Case #3, P = N, so every student will be on your team. You have to spend 6 hours training the third student, so that they have a skill of 7, like everyone else. This is the minimum time you can spend,
'''


from xmlrpc.client import MAXINT


def solution(n: int, p: int, s: list) -> int:
    '''
        Solution for the input: return integer
    '''
    min_count = MAXINT
    for i in range(n-p+1):
        max_value = max(s[i:])
        sum_list = sum(s[i:])
        current_count = max_value*p - sum_list
        if current_count < min_count:
            min_count = current_count
    
    return min_count


def filterInput(input: str):
    '''
        Filter the input and send data to package
    '''
    input_list = input.split('\n')
    test_case = int(input_list[0])
    for ith_case in range(test_case):
        ith_index = ith_case*2 + 1
        ith_n_p = input_list[ith_index].split(' ')
        ith_vals = input_list[ith_index+1].split(' ')
        n_i = int(ith_n_p[0])
        p_i = int(ith_n_p[1])
        s_i = [int(x) for x in ith_vals]
        # solve the question
        result = solution(n_i, p_i, s_i)
        print(f'result = {result}')


if __name__ == '__main__':
    input: str = '''3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7'''
    filterInput(input)
