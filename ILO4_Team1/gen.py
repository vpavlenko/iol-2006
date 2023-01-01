import os
import subprocess

subprocess.call("rm *.png", shell=True)

with open("index.html", "w") as output:
    print(
        """
<style type="text/css">
p {
  display: inline-block;
  padding-right: 20px;
}
</style>
    """,
        file=output,
    )
    for filename in sorted(os.listdir(".")):
        if filename.endswith(".mov"):
            print(filename)
            name = filename.split(".")[0]
            subprocess.call(f"ffmpeg -i {filename} {name}.mp4", shell=True)
            subprocess.call(f"ffmpeg -i {filename} {name}_%03d.png", shell=True)

            pngs = sorted(
                [
                    i
                    for i in os.listdir(".")
                    if i.startswith(name) and i.endswith(".png")
                ]
            )

            print(
                f"""<h1>{name}</h1>
<div>
            <video controls>
  <source src="{name}.mp4">
</video>
</div>

            """,
                file=output,
            )
            for png in pngs:
                print(
                    f"""<p>
<img src="{png}">
<br>
{png}
</p>
""",
                    file=output,
                )
