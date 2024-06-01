from flask import Flask, request, render_template, send_from_directory, redirect, make_response


app = Flask(__name__)
@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def serve_index():
    return render_template('index.html', content_type='text/html')

@app.route('/products>')
def serve_products():
    return render_template('products.html', content_type='text/html')

@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename, mimetype='text/css')

@app.route('/static/images/<path:filename>')
def serve_images(filename):
    extension = filename.split('.', 1)
    return send_from_directory('static/images', filename, mimetype=f'text/{extension}')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)