from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')
#creatinh home page wioth drop downs 
@app.route('/', methods=["GET", "POST"])
def index():

    region = {
        'ALASKA': ['boat1', 'boat2', 'boat3', 'boat4', 'boat5', 'boat6', 'boat7', 'boat8'],
        'HAWAII': ['boat1', 'boat2', 'boat3', 'boat4', 'boat5', 'boat6', 'boat7', 'boat8', 'boat9', 'boat10'],
        'WESTCOAST': ['boat1', 'boat2', 'boat3']
    }
    
    if request.method == "POST":

        regionGet = request.form.get("region")
        boatGet = request.form.get("boat")
        
        s = str(regionGet) + str(boatGet)
        

        return redirect('/' + s)

    return render_template('temp.html', region=region)
#creating all othe rpages to display the maps and the boats movements 

@app.route('/WESTCOAST0')
def WESTCOAST0():
    
    return render_template('westcoast0.html')             
    
@app.route('/WESTCOAST1')
def WESTCOAST1():
    
    return render_template('westcoast1.html')             

@app.route('/WESTCOAST2')
def WESTCOAST2():
    
    return render_template('westcoast2.html')     
        
@app.route('/HAWAII0')
def HAWAII0():
    
    return render_template('HAWAII0.html')   

@app.route('/HAWAII1')
def HAWAII1():
    
    return render_template('HAWAII1.html')

@app.route('/HAWAII2')
def HAWAII2():
    
    return render_template('HAWAII2.html')

@app.route('/HAWAII3')
def HAWAII3():
    
    return render_template('HAWAII3.html')

@app.route('/HAWAII4')
def HAWAII4():
    
    return render_template('HAWAII4.html')

@app.route('/HAWAII5')
def HAWAII5():
    
    return render_template('HAWAII5.html')   

@app.route('/HAWAII6')
def HAWAII6():
    
    return render_template('HAWAII6.html')

@app.route('/HAWAII7')
def HAWAII7():
    
    return render_template('HAWAII7.html')

@app.route('/HAWAII8')
def HAWAII8():
    
    return render_template('HAWAII8.html')

@app.route('/HAWAII9')
def HAWAII9():
    
    return render_template('HAWAII9.html')

@app.route('/ALASKA0')
def ALASKA0():
    
    return render_template('ALASKA0.html')

@app.route('/ALASKA1')
def ALASKA1():
    
    return render_template('ALASKA1.html')

@app.route('/ALASKA2')
def ALASKA2():
    
    return render_template('ALASKA2.html')

@app.route('/ALASKA3')
def ALASKA3():
    
    return render_template('ALASKA3.html')

@app.route('/ALASKA4')
def ALASKA4():
    
    return render_template('ALASKA4.html')   

@app.route('/ALASKA5')
def ALASKA5():
    
    return render_template('ALASKA5.html')

@app.route('/ALASKA6')
def ALASKA6():
    
    return render_template('ALASKA6.html')

@app.route('/ALASKA7')
def ALASKA7():
    
    return render_template('ALASKA7.html')

@app.route('/ALASKA8')
def ALASKA8():
    
    return render_template('ALASKA8.html')

if __name__ == '__main__':
    app.run()
