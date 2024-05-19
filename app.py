from flask import Flask, request, render_template

app = Flask(__name__)

def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]

@app.route('/', methods=['GET', 'POST'])
def flames():
    result = None
    if request.method == 'POST':
        p1 = request.form['player1'].lower().replace(" ", "")
        p2 = request.form['player2'].lower().replace(" ", "")
        p1_list = list(p1)
        p2_list = list(p2)

        proceed = True
        while proceed:
            ret_list = remove_match_char(p1_list, p2_list)
            con_list = ret_list[0]
            proceed = ret_list[1]
            star_index = con_list.index("*")
            p1_list = con_list[: star_index]
            p2_list = con_list[star_index + 1:]

        count = len(p1_list) + len(p2_list)
        result_list = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        
        while len(result_list) > 1:
            split_index = (count % len(result_list) - 1)
            if split_index >= 0:
                right = result_list[split_index + 1:]
                left = result_list[: split_index]
                result_list = right + left
            else:
                result_list = result_list[: len(result_list) - 1]
        
        result = result_list[0]
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
