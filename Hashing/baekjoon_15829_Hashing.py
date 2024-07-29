"""
15829: Hashing

입력되는 문자열: 모두 다 영문 소문자 => 1~26번까지 번호 매길 수 있음 => abba:1221
해시 함수를 구현하는 문제
문자열 혹은 수열을 하나의 정수로 치환하기
r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891(놀랍게도 소수이다!!)로 하자.

"""
import sys 

L = int(input())
string = sys.stdin.readline().strip()

# 딕셔너리 초기화
alphabets = "abcdefghijklmnopqrstuvwxyz"
num_alpha = {}
for i, s in enumerate(alphabets):
  num_alpha[s] = i+1

# 해시함수 공식
r=31
M=1234567891
total =0

for i, s in enumerate(string):
  total += num_alpha.get(s) * (r ** i)

print(total%M)