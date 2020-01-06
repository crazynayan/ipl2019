from firestore_ci import ORDER_DESCENDING
from flask import render_template, Response
from flask_login import login_required

from flask_app import ipl_app
from flask_app.player import Player
from flask_app.user import User


@ipl_app.route('/')
@ipl_app.route('/home')
@ipl_app.route('/users')
@login_required
def home() -> Response:
    users = User.objects.order_by('points', ORDER_DESCENDING).get()
    return render_template('user_list.html', title='IPL 2019', users=users)


@ipl_app.route('/users/<username>/players')
@login_required
def user_players(username: str) -> Response:
    players = Player.objects.filter_by(owner=username).get()
    players.sort(key=lambda player: -player.score)
    return render_template('player_list.html', title=f'Players owned by {username.upper()}', players=players)

