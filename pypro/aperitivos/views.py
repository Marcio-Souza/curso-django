from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'video_id': 437255932},
    {'slug': 'instalacao-windows', 'titulo': 'Video Aperitivo: Instalação Windows',
     'video_id': 437893110}
]

videos_dct = {dct['slug']: dct for dct in videos}


class Video:
    def __init__(self, slug, titulo, video_id):
        self.titulo = titulo
        self.slug = slug
        self.video_id = video_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 437255932),
    Video('instalacao-windows', 'Video Aperitivo: Instalação Windows', 437893110)
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})