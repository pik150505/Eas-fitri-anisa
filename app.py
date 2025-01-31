from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Daftar tugas (To-Do List)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Menambahkan tugas baru
        task = request.form["task"]
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete(task_id):
    # Menghapus tugas berdasarkan ID
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
