def basic():
	"""
	파이썬 알고리즘 풀기전에 기초 리마인드
	"""
	# 1. 특정 크기의 2차원 리스트를 초기화할 때 반드시 리스트 컴프리헨션을 이용
	# 1.1. N x M 크기의 2차원 리스트 초기화
	# 1.1.1. 잘못된 예시
	n = 3
	m = 4
	array = [ [0] * m ] * n
	print("result_1:", array)

	array[1][1] = 5
	print("result_2:", array)
	# -> 하나의 서브리스트 참조하여 3개의 서브리스트를 보여준 것 뿐임.

	# 1.2.3. 정확한 예시 : 리스트 컴프리헨션을 통한 2차원 리스트 초기화
	print()
	array = [
		[0] * m for _ in range(n)
	]
	print("result_3:", array)

	array[1][1] = 5
	print("result_4:", array)

	# ----------------------------------------------------
	# 리스트 자료형: 가변, 관련 주요 메서드
	# 리스트와 관련된 메서드를 사용하면 리스트 자료형을 효과적으로 이용가능
	# 메서드명 / 설명 / 시간복잡도
	# append() / 리스트에 원소 하나를 삽입할 때 사용 / O(1)
	# sort() / 오름차순 정렬 / O(NlogN)
	# sort(reverse=True) / 내림차순 정렬 / O(NlogN)
	# reverse() / 리스트의 원소 순서를 모두 뒤집는다 / O(N)
	# insert(인덱스, 값) / 특정 인덱스 위치에 원소를 삽입 / O(N)
	# count(값) / 리스트 내 특정 값의 개수 / O(N)
	# remove() 또는 (값) / 특정 값의 원소를 제거하지만, 여러개면 1개만 제거한다. / O(N)
	# 직접해보기
	print()
	array = [1, 4, 3]
	print("리스트:", array)

	# 리스트에 원소 삽입
	array.append(2)
	print("append():", array)

	# 오름차순 정렬
	array.sort()
	print("sort():", array)

	# 내림차순 정렬
	array.sort(reverse=True)
	print("sort(reverse=True):", array)

	# 리스트 원소 뒤집기
	array.reverse()
	print("reverse():", array)

	# 2번 인덱스에 정수 3 추가
	array.insert(2, 3)
	print("insert(idx, object):", array)

	# 특정 값의 데이터의 개수 세기
	# print("count() 리스트의 전체 데이터 개수:", array.count()) -> error : 이딴건 없음, 어떤 object던 개수만 알고 싶다면 len(array) 사용하면 되자너
	print("count(object) 값이 3인 데이터 개수:", array.count(3))

	# 특정 값 데이터 삭제(여러개라면 제일 좌측부터 1개만 제거)
	array.remove(3)
	print("remove(object):", array)

	# insert(), append(), remove() 함수를 주의할 것
	# insert()를 사용할 때 원소의 개수가 N개면, 시간 복잡도는 O(N)이라고 언급했다.
	# 리스트 자료형의 append()는 O(1)에 수행되는데 반해, insert()는 동작이 느리다.
	# 중간에 원소를 삽입한 뒤에, 리스트의 원소 위츠를 조정해줘야 하기 때문이다.
	# 따라서 insert()를 남발하면 시간초과로 테스트를 통과하지 못할 수도 있다.

	# remove()도 마찬가지로 리스트에서 특정 원소를 삭제한 뒤,
	# 해당 리스트의 원소 위치를 조정해줘야 하기 때문에 느리다.

	# 그렇다면 특정한 값의 원소를 모두 제거하려면 어떻게 해야할까?
	# 그냥 조건문으로 해당 값을 포함시키지 않으면 된다. 알고있잖아.
	array = [1, 2, 3, 4, 5, 5, 5]
	remove_set = {3, 5}
	array = [offset for offset in array if offset not in remove_set]
	print("remove()를 사용하지않고 빠른 시간으로 특정값 제거:", array)

	# 문자열 곱연산은 실제로 써본적이 없는 것 같아서 직접 쳐봄
	print()
	string = 'Hello'
	print("문자열 곱연산:", string * 3)
	
	# 파이썬의 문자열은 내부적으로 리스트와 같이 처리된다.
	# 문자열은 여러 개의 문자가 합쳐진 리스트라고 볼 수 있다.
	# 인덱싱과 슬라이드가 가능하다는 말이다.
	string = 'Hello'
	print(f"문자열 인덱싱, 슬라이싱: {string[1:4]}")
	print()

	# ----------------------------------------------------
	# 튜플 자료형 : 불변
	num_tuple = (1, 2, 3, 4, )
	print("튜플:", num_tuple)
	# 튜플에 어떤 원소의 값을 수정하면 에러 발생
	# 'tuple' objects does not support item assignment(튜플은 원소의 대입을 지원하지 않는다.)
	# 튜플 자료형은 주로 그래프 알고리즘을 구현할 때 사용된다.
	# 다익스트라 최단 경로 알고리즘 : 최단 경로를 찾아주는 알고리즘의 내부에서 우선순위 큐를 이용하는데,
	# 해당 알고리즘에서 우선순위 큐에 한 번 들어간 값은 변경되지 않는다.
	# 그래서 해당 우선순위 큐에 들어가는 데이터를 튜플로 구성하여 소스코드를 작성한다.
	# 튜플은 리스트에 비해 상대적으로 공간효율적이고,
	# 일반적으로는 각 원소의 성질이 서로 다를 때 주로 사용한다.
	# 다익스트라 최단 경로 알고리즘에서는 (비용, 노드번호)의 형태로 관리하는 것이 관례이다.

	# ----------------------------------------------------
	# 사전 자료형; 딕셔너리
	# 위의 리스트와 튜플은 이터러블(순차적으로 저장한다는 특징)
	# 사용법은 알고있으니 이론적으로 보자면
	# 딕셔너리는 내부적으로 Hash Table을 이용하므로 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
	# 키-값 쌍으로 구성된 데이터를 처리함에 있어서 리스트보다 훨씬 빠르게 동작한다는 점을 기억하자.

	# 코테에서의 예시로,
	# 학생의 번호가 1부터 10,000,000(천만)까지 구성되어있는 상황에서,
	# 최대 10,000명의 학생을 선택했다고 가정해보자.
	# 이후에 특정한 학생 번호가 주어졌을 때 해당 학생이 선택되었는지를 어떻게 빠르게 알 수 있을까?
	# 만약 리스트를 이용한다면, 1부터 일천만까지 각 번호가 '선택되었는지 저장할 수 있는' 리스트를 만들어야 한다.
	# 다시 말해, 일천만개 데이터를 저장할 수 있는 리스트를 만들어야 하므로 많은 메모리 공간이 낭비된다.
	# 이중 999만개 데이터는 쓰이지 않을 것이다.

	# 하지만 딕셔너리를 이용한다면, 천만개의 데이터를 담을 필요가 없으며
	# 일만개의 데이터만 딕셔너리에 들어가므로 훨씬 적은 메모리 공간을 사용할 수 있다.

	# 딕셔너리 관련 함수
	# keys(), values(), items()
	print()

	fruit_dict = {
		"사과": "Apple",
		"바나나": "Banana",
		"코코넛": "Coconut"
	}

	fruit_data_list = [
		fruit_dict.keys(),
		fruit_dict.values(),
		fruit_dict.items()
	]

	for sub_list in fruit_data_list:
		print(sub_list)

	# ----------------------------------------------------
	# 집합 자료형; set, 셋
	# 실제 사용할땐 순서보장 없이 중복제거할 때 주로 사용했었음
	# 이론적으로, 리스트 혹은 문자열을 이용해서 만들 수 있는데 이런 특징이 있다.
	# 중복을 허용하지 않음 / 순서를 보장하지 않음
	# 시간복잡도는 딕셔너리와 같이 O(1)
	
	# '특정한 데이터가 이미 등장한 적이 있는지 여부'를 체크할 때 매우 효과적이라고 한다.

	# ----------------------------------------------------
	# 반복문
	# while, for 문
	# 중첩된 반목문의 경우 코테에서 '플로이드 워셜 알고리즘, 다이나믹 프로그래밍'
	# 알고리즘 문제에서 매우 많이 사용된다

	# 구구단
	# for i in range(1, 10):
	# 	for j in range(1, 10):
	# 		print(f"{i} * {j} = {i * j}")

	# ----------------------------------------------------
	# 함수 넘어감
	# 입출력
	# 여러개의 데이터를 입력받을 때 공백으로 구분되는 경우가 많다.
	# 이때, list(map(int, input().split()))을 사용하면 됨
	# 입력받은 데이터를 split해서 공백제거 후 각각 int형변환 후 리스트에 담김

	# 입력을 위한 전형적인 코드
	
	# 받을 데이터 개수 입력받을 시
	# n = int(input())
	
	# 여러 데이터를 공백으로 구분해서 입력받을 시
	# data = list(map(int, input().split()))
	
	# 공백을 기준으로 구분하여 적은 수의 데이터 입력을 받을 시
	# n, m, k를 공백으로 구분하여 입력
	# n, m, k = map(int(input().split()))

	# 문제를 풀다보면, 입력을 최대한 빠르게 받아야 하는 경우가 있다.
	# 흔히 정렬, 이진탐색, 최단 경로 문제의 경우
	# 매우 많은 수의 데이터가 연속적으로 입력이 되곤한다.
	# 예시로 천만개가 넘는 라인이 입력되는 경우,
	# 입력을 받는 것만으로도 시간초과를 받을 수 있다.

	# 파이썬에서 입력의 개수가 많은 경우에는 input()을 그대로 사용하지는 않는다.
	# 기본 input()는 동작 속도 느려서 시간 초과로 오답 판정이 될 수 있기 때문에,
	# sys 라이브러리에 정의된 sys.stdin.readline()을 이용한다.
	# 아래와 같이 사용한다,
	# import sys
	# sys.stdin.readline().rstrip()
	# sys 라이브러리를 사용할 떄는 한 줄 입력을 받고 나서 rstrip()을 꼭
	# 호출해야한다.
	# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데,
	# 이 공백 문자를 제거하려면 꼭 사용해야한다. 관행이다. 외워야한다.

	# readline() 예시
	# import sys
	# # 문자열 입력받기
	# string = sys.stdin.readline().rstrip()
	# print(string)

	# ----------------------------------------------------
	# 주요 라이브러리 문법과 유의점
	# 표준 라이브러리란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를
	# 미리 구현해 놓은 라이브러리를 말한다.
	# 파이썬 코테를 준비하며 반드시 알아야할 라이브러리는 6가지 정도이다.
	
	# 요약 설명
	# 내장 함수: print(), input()과 같은 기본 입출력 기능부터,
	# sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리이다.

	# itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공,
	# 순열과 조합 라이브러리 제공

	# heapq = 힙(heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현
	# 하기 위해 사용

	# bisect: 이진 탐색(binary search) 기능을 제공

	# collections: deque, counter 등의 유용한 자료구조를 포함

	# math: 필수적인 수학적 기능을 제공, 팩토리얼, 제곱근, 최대공약수(GCD),
	# 삼각함수 관련, pi와 같은 상수를 포함

	
	