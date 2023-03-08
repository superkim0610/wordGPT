import tkinter

import gpt_request
import tkinter
import tkinter.ttk
import time  # test

root = 0
wordEntry = 0

def wordAddBtnClicked():
    word = wordEntry.get()
    bn = "\n"

    print(word)
    recommendedWords = gpt_request.getWords(word, 3)
    recommendedWordlableText = f"<유의어>\n{bn.join(recommendedWords['syntonyms'])}" + bn * 2 + f"<반의어>\n{bn.join(recommendedWords['antonyms'])}" + bn * 2 + f"<추천 단어>\n{bn.join(recommendedWords['recommendations'])}"
    recommendedWordLable = tkinter.Label(root, text=recommendedWordlableText)
    recommendedWordLable.pack()

    exampleSentences = gpt_request.getSentences(word, 2)
    exampleSentencesLableText = f"\n<예문>\n{bn.join(exampleSentences)}"
    exampleSentencesLable = tkinter.Label(root, text=exampleSentencesLableText)
    exampleSentencesLable.pack()


def main():
    global root, wordEntry
    root = tkinter.Tk()
    root.title("pyTodo")
    root.geometry("640x480+300+300")
    root.resizable(False, False)

    # treeview = tkinter.ttk.Treeview(root, columns=["index", "word", "meaning"], displaycolumns=["index", "word", "meaning"])
    # # treeview.pack()
    #
    # # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    # treeview.column("index", width=50, anchor="center")
    # treeview.heading("index", text="순서", anchor="center")
    #
    # treeview.column("word", width=200, anchor="center")
    # treeview.heading("word", text="단어", anchor="center", command=foo)
    #
    # treeview.column("meaning", width=200, anchor="center")
    # treeview.heading("meaning", text="뜻", anchor="center")
    #
    # treeview["show"] = "headings"
    #
    # # 표에 삽입될 데이터
    # treelist = [(1,"apple", "사과"), (2,"penetrate", "관통하다"),(3,"vegetable", "야채")]
    #
    # # 표에 데이터 삽입
    # for i in range(len(treelist)):
    #     treeview.insert('', 'end', text="", values=treelist[i], iid=i)

    wordEntry = tkinter.Entry(root, width=20)
    wordEntry.pack()

    wordAddBtn = tkinter.Button(root, width=3, text="+", command=wordAddBtnClicked)
    wordAddBtn.pack()

    root.mainloop()


def test():
    t = time.time()
    print(gpt_request.getWords("happy", 5))
    print(time.time() - t)

    t = time.time()
    print(gpt_request.getSentences("happy", 5))
    print(time.time() - t)


if __name__ == "__main__":
    main()
    # test()
