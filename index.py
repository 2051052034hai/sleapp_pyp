from flask import render_template, request
from saleapp_ import app
import utils

@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', catgories=cates)

@app.route("/product")
def product_list():
    kw = request.args.get("keyword")
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    cate_id = request.args.get("category_id")
    product = utils.load_products(cate_id=cate_id,kw=kw,from_price=from_price, to_price=to_price)
    return render_template('product.html', product_=product)


#Path params
@app.route("/hello/<int:name>")
def hello(name):
    return  render_template('index.html',
                        message = "XIN CHAO %s!!!" %name)

@app.route("/hello")
def hello2():
    fn = request.args.get('first', 'a')
    ln = request.args.get('last', 'b')

    return render_template('index.html',
                            message=" Wellcome to " + str(fn) + str(ln))

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = utils.product_by_id(product_id)
    return render_template('product_detail.html', product = product)
if __name__ == '__main__':
    app.run(debug=True)