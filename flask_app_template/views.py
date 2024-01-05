from . import app, oidc
from flask import render_template, redirect, url_for, jsonify, request



@app.route('/', methods=["GET"])
def index_route():
    if oidc.user_loggedin:
        return render_template('index.html', logged_in=True, user=oidc.user_getinfo(['email', 'username', 'profile']))
    else:
        return render_template('index.html', logged_in=False)


@app.route('/app', methods=["GET"])
def app_route():
    if oidc.user_loggedin:
        return render_template('app.html', logged_in=True, user=oidc.user_getinfo(['email', 'username', 'profile']))
    else:
        return redirect('/login?next=' + url_for('app_route', _external=True))
    


@app.route('/test_app', methods=["POST"])
def test_app_route():
    if oidc.user_loggedin:
        secret_data_from_python = "secret"
        sent_data = request.json
        response_data = {
            "secret_data_from_python": secret_data_from_python,
            "sent_data": sent_data
        }
        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Unauthorized'}), 401


@app.route('/login', methods=["GET"])
def login():
    oidc.redirect_to_auth_server()


@app.route('/oidc/callback')
def oidc_callback():
    if oidc.user_loggedin:
        return redirect('/')
    else:
        return jsonify({'error': 'Login failed'}), 401


@app.route('/logout')
def logout():
    oidc.logout()
    oidc_provider_logout_url = 'https://<keycloak_url>/realms/<realm_name>/protocol/openid-connect/logout'
    post_logout_redirect_uri = '/'
    logout_url = f'{oidc_provider_logout_url}?redirect_uri={post_logout_redirect_uri}'
    return redirect(logout_url)
