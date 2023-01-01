import os
import subprocess

subprocess.call("rm *.png", shell=True)

CSS_RULES = """
<style type="text/css">
p {
  display: inline-block;
  padding-right: 20px;
}
</style>
"""

with open("index.html", "w") as output:
    print(
        CSS_RULES,
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

            VIDEO_EMBED = f"""<h1>{name}</h1>
<div>
            <video controls>
  <source src="{name}.mp4">
</video>
</div>
            """

            VIDEO_CONTENT = [VIDEO_EMBED]

            for png in pngs:
                VIDEO_CONTENT.append(
                    f"""<p>
<img src="{png}">
<br>
{png}
</p>
"""
                )

            print(
                "\n".join(VIDEO_CONTENT),
                file=output,
            )

            with open(f"{name}.html", "w") as single_video_output:
                print(CSS_RULES, file=single_video_output)
                print(
                    "\n".join(VIDEO_CONTENT),
                    file=single_video_output,
                )
