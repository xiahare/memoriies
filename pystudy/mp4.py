from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

VIDEO_FOLDER_BIRTH66 = os.path.join('static', 'birth66')
VIDEO_FOLDER_WEDDING = os.path.join('static', 'wedding')
app.config['birth66'] = VIDEO_FOLDER_BIRTH66
app.config['wedding'] = VIDEO_FOLDER_WEDDING


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<subpath>')
def catalog(subpath):
    VIDEO_FOLDER = app.config[subpath]
    video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith('.mp4')]
    return render_template(subpath+'/index.html', video_files=video_files, subpath=subpath)

@app.route('/play/<subpath>/<filename>')
def play(subpath,filename):
    return send_from_directory(app.config[subpath], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)