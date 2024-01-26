from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will be our in-memory tasks list
tasks = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        tasks.append(task_content)
        return redirect(url_for("index"))
    else:
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    try:
        tasks.pop(task_id)
    except IndexError:
        pass  # Handle the error if we try to delete a non-existent task
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=4999, debug=True)
