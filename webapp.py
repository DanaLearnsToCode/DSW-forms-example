from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
   
@app.route("/response")
def render_response():
    answer1 = request.args['answer1'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if answer1 == 'yes':
        reply = "I like movies, too!"
        return render_template('response.html', response = reply)
    else:
        reply = "Good to know because I do like movies"
        return render_template('response2.html', response = reply)

@app.route("/response2")
def render_response2():
    answer2 = request.args['answer2']
    if answer2 == "horror":
        reply = "That's cool! My friend was one of the main actors in La Larona. If you haven't watched it it's pretty scary."
        return render_template('response31.html', response = reply)
    if answer2 == "comedy":
        reply = "I also prefer comedy because I like to laugh, but horror movies are still fun to watch"
        return render_template('response32.html', response = reply)
    if answer2 == "yes":
         reply = "I'm also a sports person."
         return render_template('response33.html', response = reply)
    if answer2 == "no":
         reply = "Wow! most people I know play sports, so this is very cool."
         return render_template('response34.html', response = reply)
            

#@app.route("/home2.html")
#def render_main():
#    return render_template('home2.html')

#@app.route("/response2")
#def render_response2():
#    answer2 = request.args['answer2']
#    if answer2== 'comedy':
#        reply = "I prefer comedy because I like to laugh, but horror movies are still fun to watch"
#    else answer2== 'horror':
#        reply = "That's cool! Did you know that my friend starred in La Larona. If you haven't watched it it's pretty scary."
#    return rendertemplate('response2.html', response = reply)
        
        
                     
if __name__=="__main__":
    app.run(debug=False, port=54321)
