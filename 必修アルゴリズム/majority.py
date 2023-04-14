
vote = [
"山田太郎", "鈴木花子", "佐藤三郎", "鈴木花子",
"鈴木花子", "佐藤三郎", "鈴木花子", "佐藤三郎",
"鈴木花子", "鈴木花子", "山田太郎", "鈴木花子"
]

half = len(vote) // 2

vote.sort()

if vote.count(vote[half]) > half:
    print(vote[half])
else:
    print("No")
    