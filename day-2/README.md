# Day Two

## Lesson - ???

### Item One

## Recap

## Exercises

## BONUS: Embedding Youtube Content

Go to http://youtube.com and find a video to your liking. Note that some videos cannot be embedded and you generally won't know until you attempt to embed it.

Under the `Share` option choose `Embed` and copy paste the iframe into one of your views. It will look something like this:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/ABCD1234" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

The video should now appear whenever you render that view. An important thing to notice about the youtube video is each video has an id. Inside the url for the embed (for example: `https://www.youtube.com/embed/ABCD1234`) you will be able to find that particular id (for example: `ABCD1234`).

We can set up our player to dynamically render a video or videos:

```python
def render_favorite_videos(request):
    context = {
        fav_videos: [
            'ABCD1234',
            'EFGH5678',
            'IJKL9012'
        ]
    }
    return render(request, 'app_name/youtube_videos.html', context)
```

And inside the template:

```html
{% for video_id in fav_videos %}

<iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video_id }}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

{% endfor %}
```

Notice where we've used the variable tags inside the loop.