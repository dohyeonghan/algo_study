# # 1
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def solution(stack1, stack2, stack3):
#     candi = []
#     answer = ''
#     if len(stack1) > 0:
#         for s1 in stack1:
#             candi.append((s1,1))
#     if len(stack2) > 0:
#         for s2 in stack2:
#             candi.append((s2,2))
#     if len(stack3) > 0:
#         for s3 in stack3:
#             candi.append((s3,3))
#     candi.sort(key=lambda x: -x[0])
#     for n,s in candi:
#         answer += str(s)
#     return answer
#
# # 2
# import spacy
#
#
# # sentences = ['John is old','Mark Oldham ate an apple'
# s = 'Mark Oldham ate an apple'
#
#
# nlp = spacy.load("en_core_web_sm")
#
# def anonymize_text(sentences):
#     doc = nlp(sentences)
#     candi = list(sentences)
#     print(candi)
#     idx_list = []
#     for d in doc.ents:
#         idx_list.append((d.start_char, d.end_char))
#         # print(d.start_char, d.end_char)
#         # tmp = list(d.text)
#         # print(tmp)
#         # for i in range(len(tmp)):
#         #     tmp[i] = 'X'
#         # tmp = ''.join(tmp)
#         # print(tmp)
#     print(idx_list)
#     for idx in idx_list:
#         for i in range(idx[0],idx[1]):
#             candi[i] = 'X'
#     print(candi)
#     candi = ''.join(candi)
#     print(candi)
#
#
#     return ''
# anonymize_text(s)

# 3
# strs = 'aabcba'
# s_dict = {}
#
#
#
# print(s_dict)
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
S = 'aabcba'
C = [1,3,2]
def solution(S, C):
    # write your code in Python 3.8.10
    s_dict = {}
    for i in range(len(S)):
        if S[i] not in s_dict:
            s_dict[S[i]] = [i]
        else:
            s_dict[S[i]].append(i)

    zero_check = False
    for value in s_dict.values():
        if len(value) > 0:
            zero_check = True
    if zero_check == False:
        return 0

    for c in C:
        for key, value in s_dict.items():
            if key == ''



solution(S,C)
