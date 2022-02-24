# def join_rev_strings(strings):
#     s = ''
#     result = []
#     n_strings = len(strings)
#     for i in range(n_strings):
#         if i == 0:
#             result.append(strings[i].rstrip(' ').swapcase())
#         elif i == n_strings - 1:
#             result.append(strings[i].lstrip(' ').swapcase())
#         else:
#             result.append(strings[i].strip(' ').swapcase())

#     for s in result:
#         if len(s) == 0:
#             del s
#     return " ".join(result)[::-1]

def is_not_empty(s):
    return len(s) > 0

def join_rev_strings(strings):
    # print(strings)
    result = [s for s in strings if is_not_empty(s.strip(' '))]
    n_strings = len(result)
    # print(n_strings)
    # print(result)
    if n_strings == 0:
        return ''
    elif n_strings == 1:
        return result[0].swapcase()[::-1]
    else:
        for i in range(n_strings):
            # print(i)
            if i == 0:
                # print(i)
                # print(result[i])
                result[i] = result[i].rstrip(' ').swapcase()
            elif i == n_strings - 1:
                result[i] = result[i].lstrip(' ').swapcase()
            else:
                result[i] = result[i].strip(' ').swapcase()
        # print(" ".join(result)[::-1])
        return " ".join(result)[::-1]

def exec(argv):
    if len(argv) == 1:
        return f"Usage: {argv[0]} STRING..."
    elif len(argv) == 2:
        return argv[1].swapcase()[::-1]
    else:
        return join_rev_strings(argv[1:])


# if __name__ == "__main__":
#     argv = ["exec.py"]
#     # argv.extend(['L337   ', '5P3AK!   '])
#     argv.extend(['', 'L337', '5P3AK!'])
#     print(exec(argv))

