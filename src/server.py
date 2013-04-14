import os

from flask import Flask, request, Response, abort
from flask import render_template

import database
import apis
from auth import requires_auth
from src import facade


app = Flask(__name__)
DEFAULT_PATH = 'index.html'
MIMES = {
    'css': 'text/css',
    'html': 'text/html',
    'ico': 'image-x-icon',
    'jpg': 'image/jpeg',
    'js': 'application/javascript',
    'json': 'application/json',
    'png': 'image/png',
    'mp3': 'audio/mpeg',
}

"""
Index view
"""
@app.route('/')
@app.route('/<path:path>')
def serve(path=DEFAULT_PATH):
    """
    """
    if not os.path.exists(path):
        abort(404)
    content = file(path, 'r').read()
    mimetype = MIMES[path[path.rindex('.') + 1:]]
    return Response(content, status=200, mimetype=mimetype)
"""
Dishes

"""
@app.route('/dishes')
def serve_dishes():
    return render_template("dishes.html")

@app.route('/dishes/<dishType>')
def serve_dish_type_list(dishType):
    dishes = facade.get_dishes_by_type(dishType)
    return render_template('dish-list.html', dishes=dishes)


@app.route('/admin/dishes')
def serve_admin_dishes():
    dishes = facade.get_dishes()
    return render_template('admin-dishes.html', dishes=dishes)

@app.route('/admin/dishes', methods=['POST'])
def serve_add_dish():
    name = request.form['name']
    price = request.form['price']
    image = request.form['image']
    description = request.form['description']
    dishType = request.form['dishType']
    facade.create_dish(name,price,image,description,dishType)
    return Response('Created.', status=201, mimetype='text/html')


@app.route('/admin/dishes/<id>', methods=['DELETE'])
def serve_delete_dish(id):
    facade.remove_dish(id)
    return Response('No Content.', status=204, mimetype='text/html')

"""
Menus
"""

@app.route('/menus')
def serve_menus():
    menus = facade.get_menus()
    return render_template('menus.html',menus = menus)

@app.route('/admin/menus')
def serve_admin_menus():
    menus = facade.get_menus()
    dishes = facade.get_dishes()
    return render_template('admin-menus.html', menus = menus, dishes = dishes)

@app.route('/admin/menus', methods=['POST'])
def serve_add_menu():
    name = request.form['name']
    price = request.form['price']
    dishes = []
    dishes.append(database.get_dish_by_id(request.form['dish1']))
    dishes.append(database.get_dish_by_id(request.form['dish2']))
    dishes.append(database.get_dish_by_id(request.form['dish3']))
    description = request.form['description']
    facade.create_menu(name,price,dishes,description)
    return Response('Created!', status=201, mimetype='text/html')

@app.route('/admin/menus/<id>', methods=['DELETE'])
def serve_delete_menu(id):
    facade.remove_menu_by_id(id)
    return Response('No Content.', status=204, mimetype='text/html')

"""
Users
"""

@app.route('/admin/users')
def serve_users():
    users = facade.get_users()
    print users

    return render_template('admin-user.html', users = users)

@app.route('/admin/users', methods=['POST'])
def serve_add_user():
    user_name =  request.form['name']
    password = request.form['password']
    print user_name,password
    facade.create_user(user_name, password)
    return Response('Created.', status=201, mimetype='text/html')

@app.route('/admin/users/<user_name>' , methods=['DELETE'])
def serve_delete_user(user_name):
    facade.remove_user_by_name(user_name)
    return Response('No Content.', status=204, mimetype='text/html')

"""
Reservations

"""

@app.route('/reservations.html')
@app.route('/templates/reservations.html')
@requires_auth
def serve_reservations():
    return render_template('reservations.html')

@app.route('/reservations', methods=['POST'])
@requires_auth
def serve_add_reservation():
    name = request.form['name']
    date = request.form['date']
    chairs = request.form['name']
    facade.create_reservation(name,chairs,date)
    data = {
        "name" : name,
        "date" : date
    }

    print data
    return render_template('accepted.html', data = data)


"""
Instagram integration
"""
@app.route('/instafood')
def serve_instagram_pics():
    links = apis.get_instagram_pics()
    return render_template('instagram.html', links = links)




if __name__ == '__main__':
    app.run('0.0.0.0', port=9001, debug=True)

