def reverseMessage(message: str) -> str:
    message = message.strip()  # 移除字符串左右两侧的空余字符
    left = right = len(message) - 1
    res = []
    while left >= 0:
        while left >= 0 and message[left] != ' ':
            left -= 1
        res.append(message[left + 1: right + 1])
        while message[left] == ' ':
            left -= 1
        right = left
    return ' '.join(res)

message = "the sky is blue"
res = reverseMessage(message)
print(res)