{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":["b"],"id":38},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["o"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["k"],"id":39}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"remove","lines":["s"],"id":40},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"remove","lines":["k"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"remove","lines":["s"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"remove","lines":["a"]}],[{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"remove","lines":["t"],"id":41}],[{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["b"],"id":42},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["o"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["o"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["k"]}],[{"start":{"row":7,"column":176},"end":{"row":7,"column":177},"action":"remove","lines":["'"],"id":43},{"start":{"row":7,"column":175},"end":{"row":7,"column":176},"action":"remove","lines":["t"]},{"start":{"row":7,"column":174},"end":{"row":7,"column":175},"action":"remove","lines":["s"]},{"start":{"row":7,"column":173},"end":{"row":7,"column":174},"action":"remove","lines":["o"]},{"start":{"row":7,"column":172},"end":{"row":7,"column":173},"action":"remove","lines":["h"]},{"start":{"row":7,"column":171},"end":{"row":7,"column":172},"action":"remove","lines":["l"]},{"start":{"row":7,"column":170},"end":{"row":7,"column":171},"action":"remove","lines":["a"]},{"start":{"row":7,"column":169},"end":{"row":7,"column":170},"action":"remove","lines":["c"]},{"start":{"row":7,"column":168},"end":{"row":7,"column":169},"action":"remove","lines":["o"]},{"start":{"row":7,"column":167},"end":{"row":7,"column":168},"action":"remove","lines":["l"]},{"start":{"row":7,"column":166},"end":{"row":7,"column":167},"action":"remove","lines":["/"]},{"start":{"row":7,"column":165},"end":{"row":7,"column":166},"action":"remove","lines":["/"]},{"start":{"row":7,"column":164},"end":{"row":7,"column":165},"action":"remove","lines":[":"]},{"start":{"row":7,"column":163},"end":{"row":7,"column":164},"action":"remove","lines":["b"]},{"start":{"row":7,"column":162},"end":{"row":7,"column":163},"action":"remove","lines":["d"]}],[{"start":{"row":7,"column":161},"end":{"row":7,"column":162},"action":"remove","lines":["o"],"id":44},{"start":{"row":7,"column":160},"end":{"row":7,"column":161},"action":"remove","lines":["g"]},{"start":{"row":7,"column":159},"end":{"row":7,"column":160},"action":"remove","lines":["n"]},{"start":{"row":7,"column":158},"end":{"row":7,"column":159},"action":"remove","lines":["o"]},{"start":{"row":7,"column":157},"end":{"row":7,"column":158},"action":"remove","lines":["m"]},{"start":{"row":7,"column":156},"end":{"row":7,"column":157},"action":"remove","lines":["'"]},{"start":{"row":7,"column":155},"end":{"row":7,"column":156},"action":"remove","lines":[" "]}],[{"start":{"row":7,"column":154},"end":{"row":7,"column":155},"action":"remove","lines":[","],"id":45},{"start":{"row":7,"column":153},"end":{"row":7,"column":154},"action":"remove","lines":["'"]}],[{"start":{"row":7,"column":153},"end":{"row":7,"column":154},"action":"insert","lines":["'"],"id":46}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["v"],"id":47},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["n"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"remove","lines":["e"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"remove","lines":["t"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"remove","lines":["e"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"remove","lines":["g"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"remove","lines":["."],"id":48},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"remove","lines":["s"]},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"remove","lines":["o"]}],[{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"remove","lines":["g"],"id":49}],[{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"insert","lines":["G"],"id":50}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":23},"action":"remove","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'book_manager'","app.config[\"MONGO_URI\"] = ('mongodb+srv://Elizabeth24602:Gavroche24602@myfirstcluster-xtdqk.mongodb.net/book_manager?retryWrites=true&w=majority')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_book')","def get_book():","    return render_template(\"forum1.html\", book=mongo.db.book.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":51}],[{"start":{"row":0,"column":0},"end":{"row":37,"column":23},"action":"insert","lines":["from os import path","if path.exists(\"env.py\"):","    import env","","","import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId ","","app = Flask(__name__)","app.config[\"MONGO_DBNAME\"] = 'book_manager'","app.config[\"MONGO_URI\"] = ('mongodb+srv://Elizabeth24602:Gavroche24602@myfirstcluster-xtdqk.mongodb.net/book_manager?retryWrites=true&w=majority')","","mongo = PyMongo(app)","","","@app.route('/')","@app.route('/get_book')","def get_book():","    return render_template(\"book.html\", book=mongo.db.book.find())","    ","@app.route('/add_book')","def add_book():","    return render_template('addbook.html',","                            categories=mongo.db.categories.find())","","@app.route('/insert_book', methods=['POST'])","def insert_book():","    tasks = mongo.db.tasks","    tasks.insert_one(request.form.to_dict())","    return redirect(url_for('get_book'))","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":52}],[{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"remove","lines":["k"],"id":53},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"remove","lines":["o"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["o"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["b"]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["f"],"id":54},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["o"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["r"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["u"]}],[{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["m"],"id":55},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["1"]}],[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"remove","lines":["s"],"id":56},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"remove","lines":["k"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"remove","lines":["s"]},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"remove","lines":["a"]}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"remove","lines":["t"],"id":57}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["b"],"id":58},{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["o"]},{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["o"]},{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["k"]}],[{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":[" "],"id":59}],[{"start":{"row":20,"column":42},"end":{"row":20,"column":44},"action":"insert","lines":["\"\""],"id":60}],[{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"insert","lines":["i"],"id":61}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"insert","lines":["n"],"id":62},{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"insert","lines":["d"]},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"insert","lines":["x"],"id":63},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"insert","lines":["1"]}],[{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"insert","lines":["."],"id":64}],[{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"insert","lines":["h"],"id":65},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"insert","lines":["m"],"id":66},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"insert","lines":["l"]}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"insert","lines":[","],"id":67}],[{"start":{"row":20,"column":55},"end":{"row":20,"column":56},"action":"remove","lines":[","],"id":68},{"start":{"row":20,"column":54},"end":{"row":20,"column":55},"action":"remove","lines":["\""]},{"start":{"row":20,"column":53},"end":{"row":20,"column":54},"action":"remove","lines":["l"]},{"start":{"row":20,"column":52},"end":{"row":20,"column":53},"action":"remove","lines":["m"]},{"start":{"row":20,"column":51},"end":{"row":20,"column":52},"action":"remove","lines":["t"]}],[{"start":{"row":20,"column":50},"end":{"row":20,"column":51},"action":"remove","lines":["h"],"id":69},{"start":{"row":20,"column":49},"end":{"row":20,"column":50},"action":"remove","lines":["."]},{"start":{"row":20,"column":48},"end":{"row":20,"column":49},"action":"remove","lines":["1"]},{"start":{"row":20,"column":47},"end":{"row":20,"column":48},"action":"remove","lines":["x"]},{"start":{"row":20,"column":46},"end":{"row":20,"column":47},"action":"remove","lines":["e"]},{"start":{"row":20,"column":45},"end":{"row":20,"column":46},"action":"remove","lines":["d"]}],[{"start":{"row":20,"column":44},"end":{"row":20,"column":45},"action":"remove","lines":["n"],"id":70},{"start":{"row":20,"column":43},"end":{"row":20,"column":44},"action":"remove","lines":["i"]},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"remove","lines":["\""]}],[{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"remove","lines":[" "],"id":71}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":72}],[{"start":{"row":16,"column":0},"end":{"row":18,"column":41},"action":"insert","lines":["@app.route('/')","def index():      ","    return render_template(\"index.html\") "],"id":73}],[{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"insert","lines":["1"],"id":74}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"remove","lines":["    "],"id":75}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":76}],[{"start":{"row":16,"column":15},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":77}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":87},"action":"insert","lines":["https://4e4973316b37491ea38381cf1fa616a5.vfs.cloud9.us-east-1.amazonaws.com/index1.html"],"id":78}],[{"start":{"row":17,"column":86},"end":{"row":17,"column":87},"action":"remove","lines":["l"],"id":79},{"start":{"row":17,"column":85},"end":{"row":17,"column":86},"action":"remove","lines":["m"]},{"start":{"row":17,"column":84},"end":{"row":17,"column":85},"action":"remove","lines":["t"]},{"start":{"row":17,"column":83},"end":{"row":17,"column":84},"action":"remove","lines":["h"]},{"start":{"row":17,"column":82},"end":{"row":17,"column":83},"action":"remove","lines":["."]}],[{"start":{"row":17,"column":81},"end":{"row":17,"column":82},"action":"remove","lines":["1"],"id":80},{"start":{"row":17,"column":80},"end":{"row":17,"column":81},"action":"remove","lines":["x"]},{"start":{"row":17,"column":79},"end":{"row":17,"column":80},"action":"remove","lines":["e"]},{"start":{"row":17,"column":78},"end":{"row":17,"column":79},"action":"remove","lines":["d"]},{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":["n"]},{"start":{"row":17,"column":76},"end":{"row":17,"column":77},"action":"remove","lines":["i"]},{"start":{"row":17,"column":75},"end":{"row":17,"column":76},"action":"remove","lines":["/"]},{"start":{"row":17,"column":74},"end":{"row":17,"column":75},"action":"remove","lines":["m"]},{"start":{"row":17,"column":73},"end":{"row":17,"column":74},"action":"remove","lines":["o"]},{"start":{"row":17,"column":72},"end":{"row":17,"column":73},"action":"remove","lines":["c"]},{"start":{"row":17,"column":71},"end":{"row":17,"column":72},"action":"remove","lines":["."]},{"start":{"row":17,"column":70},"end":{"row":17,"column":71},"action":"remove","lines":["s"]},{"start":{"row":17,"column":69},"end":{"row":17,"column":70},"action":"remove","lines":["w"]},{"start":{"row":17,"column":68},"end":{"row":17,"column":69},"action":"remove","lines":["a"]},{"start":{"row":17,"column":67},"end":{"row":17,"column":68},"action":"remove","lines":["n"]},{"start":{"row":17,"column":66},"end":{"row":17,"column":67},"action":"remove","lines":["o"]},{"start":{"row":17,"column":65},"end":{"row":17,"column":66},"action":"remove","lines":["z"]},{"start":{"row":17,"column":64},"end":{"row":17,"column":65},"action":"remove","lines":["a"]},{"start":{"row":17,"column":63},"end":{"row":17,"column":64},"action":"remove","lines":["m"]},{"start":{"row":17,"column":62},"end":{"row":17,"column":63},"action":"remove","lines":["a"]},{"start":{"row":17,"column":61},"end":{"row":17,"column":62},"action":"remove","lines":["."]},{"start":{"row":17,"column":60},"end":{"row":17,"column":61},"action":"remove","lines":["1"]},{"start":{"row":17,"column":59},"end":{"row":17,"column":60},"action":"remove","lines":["-"]},{"start":{"row":17,"column":58},"end":{"row":17,"column":59},"action":"remove","lines":["t"]},{"start":{"row":17,"column":57},"end":{"row":17,"column":58},"action":"remove","lines":["s"]},{"start":{"row":17,"column":56},"end":{"row":17,"column":57},"action":"remove","lines":["a"]},{"start":{"row":17,"column":55},"end":{"row":17,"column":56},"action":"remove","lines":["e"]},{"start":{"row":17,"column":54},"end":{"row":17,"column":55},"action":"remove","lines":["-"]},{"start":{"row":17,"column":53},"end":{"row":17,"column":54},"action":"remove","lines":["s"]},{"start":{"row":17,"column":52},"end":{"row":17,"column":53},"action":"remove","lines":["u"]},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"remove","lines":["."]},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"remove","lines":["9"]},{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"remove","lines":["d"]},{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"remove","lines":["u"]},{"start":{"row":17,"column":47},"end":{"row":17,"column":48},"action":"remove","lines":["o"]},{"start":{"row":17,"column":46},"end":{"row":17,"column":47},"action":"remove","lines":["l"]},{"start":{"row":17,"column":45},"end":{"row":17,"column":46},"action":"remove","lines":["c"]},{"start":{"row":17,"column":44},"end":{"row":17,"column":45},"action":"remove","lines":["."]},{"start":{"row":17,"column":43},"end":{"row":17,"column":44},"action":"remove","lines":["s"]},{"start":{"row":17,"column":42},"end":{"row":17,"column":43},"action":"remove","lines":["f"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"remove","lines":["v"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"remove","lines":["."]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"remove","lines":["5"]},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"remove","lines":["a"]},{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"remove","lines":["6"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"remove","lines":["1"]},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"remove","lines":["6"]}],[{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"remove","lines":["a"],"id":81},{"start":{"row":17,"column":33},"end":{"row":17,"column":34},"action":"remove","lines":["f"]},{"start":{"row":17,"column":32},"end":{"row":17,"column":33},"action":"remove","lines":["1"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"remove","lines":["f"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"remove","lines":["c"]},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"remove","lines":["1"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"remove","lines":["8"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"remove","lines":["3"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"remove","lines":["8"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"remove","lines":["3"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"remove","lines":["a"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"remove","lines":["e"]},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"remove","lines":["1"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"remove","lines":["9"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"remove","lines":["4"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":["7"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["3"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["b"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["6"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["1"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"remove","lines":["3"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"remove","lines":["3"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"remove","lines":["7"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["9"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"remove","lines":["4"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"remove","lines":["e"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["4"]}],[{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["/"],"id":82},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["/"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":[":"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["s"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"remove","lines":["p"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"remove","lines":["t"]},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"remove","lines":["t"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["h"]},{"start":{"row":16,"column":15},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["i"],"id":83},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["d"],"id":84},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["x"],"id":85},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["1"]}],[{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"remove","lines":["k"],"id":86},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"remove","lines":["o"]},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"remove","lines":["o"]},{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"remove","lines":["b"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"remove","lines":["_"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"remove","lines":["t"]}],[{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"remove","lines":["e"],"id":87},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"remove","lines":["g"]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["f"],"id":88}],[{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["o"],"id":89}],[{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["r"],"id":90},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["u"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["m"],"id":91}],[{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["1"],"id":92}],[{"start":{"row":21,"column":19},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":93}],[{"start":{"row":21,"column":19},"end":{"row":22,"column":0},"action":"remove","lines":["",""],"id":94}],[{"start":{"row":18,"column":42},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":95},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":22,"column":42},"action":"insert","lines":["@app.route('/index1')","def index():      ","    return render_template(\"index1.html\") "],"id":96}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"remove","lines":["x"],"id":97},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"remove","lines":["e"]},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"remove","lines":["d"]},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"remove","lines":["n"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"remove","lines":["i"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["a"],"id":98},{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["b"]}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["o"],"id":99},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["u"]}],[{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["t"],"id":100}],[{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"remove","lines":["x"],"id":101},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["e"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["d"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["n"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["i"]}],[{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"insert","lines":["a"],"id":102},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"insert","lines":["b"]}],[{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"insert","lines":["o"],"id":103},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"insert","lines":["u"]}],[{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"insert","lines":["t"],"id":104}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":105}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"remove","lines":["x"],"id":106},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"remove","lines":["e"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"remove","lines":["d"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"remove","lines":["n"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["a"],"id":107},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["b"]}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["o"],"id":108},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["u"]}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["t"],"id":109}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":110},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":24,"column":0},"end":{"row":26,"column":42},"action":"insert","lines":["@app.route('/index1')","def index():      ","    return render_template(\"index1.html\") "],"id":111}],[{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"remove","lines":["1"],"id":112},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"remove","lines":["x"]},{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"remove","lines":["e"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"remove","lines":["d"]},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"remove","lines":["n"]}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"remove","lines":["i"],"id":113}],[{"start":{"row":26,"column":28},"end":{"row":26,"column":29},"action":"insert","lines":["c"],"id":114},{"start":{"row":26,"column":29},"end":{"row":26,"column":30},"action":"insert","lines":["h"]},{"start":{"row":26,"column":30},"end":{"row":26,"column":31},"action":"insert","lines":["o"]}],[{"start":{"row":26,"column":31},"end":{"row":26,"column":32},"action":"insert","lines":["i"],"id":115},{"start":{"row":26,"column":32},"end":{"row":26,"column":33},"action":"insert","lines":["c"]}],[{"start":{"row":26,"column":33},"end":{"row":26,"column":34},"action":"insert","lines":["e"],"id":116},{"start":{"row":26,"column":34},"end":{"row":26,"column":35},"action":"insert","lines":["s"]},{"start":{"row":26,"column":35},"end":{"row":26,"column":36},"action":"insert","lines":["1"]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"remove","lines":["x"],"id":117},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"remove","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"remove","lines":["d"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"remove","lines":["n"]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["c"],"id":118},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["h"]}],[{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["o"],"id":119},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["c"],"id":120},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["e"]},{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"remove","lines":["x"],"id":121},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"remove","lines":["e"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"remove","lines":["d"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"remove","lines":["n"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"remove","lines":["i"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["c"],"id":122},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["h"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["o"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["i"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["c"]}],[{"start":{"row":24,"column":13},"end":{"row":24,"column":19},"action":"remove","lines":["choic1"],"id":123},{"start":{"row":24,"column":13},"end":{"row":24,"column":21},"action":"insert","lines":["choices1"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":15},"action":"remove","lines":["@app.route('/')"],"id":124}],[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":125}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":126}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":15},"action":"insert","lines":["@app.route('/')"],"id":127}],[{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":128}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":34},"action":"insert","lines":["from bson.objectid import ObjectId"],"id":129}],[{"start":{"row":43,"column":40},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":130},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":4},"end":{"row":50,"column":53},"action":"insert","lines":["@app.route('/edit_task/<task_id>')","def edit_task(task_id):","    the_task =  mongo.db.tasks.find_one({\"_id\": ObjectId(task_id)})","    all_categories =  mongo.db.categories.find()","    return render_template('edittask.html', task=the_task,","                           categories=all_categories)"],"id":131}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "],"id":132}],[{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"remove","lines":["s"],"id":133},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"remove","lines":["k"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"remove","lines":["s"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"remove","lines":["a"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"remove","lines":["t"]}],[{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["b"],"id":134},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":["o"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"insert","lines":["o"]}],[{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"insert","lines":["k"],"id":135}],[{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"remove","lines":["k"],"id":136},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"remove","lines":["s"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"remove","lines":["a"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"remove","lines":["t"]}],[{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["b"],"id":137},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["o"]},{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["o"]}],[{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"insert","lines":["k"],"id":138}]]},"ace":{"folds":[],"scrolltop":121.125,"scrollleft":0,"selection":{"start":{"row":49,"column":36},"end":{"row":49,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1582820152580,"hash":"ea0fda4abe5d0066eb40f7347b4540747d8f49d5"}