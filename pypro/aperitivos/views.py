from django.shortcuts import render

# Listagem de vídeos
videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'video_id': 437255932},
    {'slug': 'instalacao-windows', 'titulo': 'Video Aperitivo: Instalação Windows',
     'video_id': 437893110}
]

videos_dct = {dct['slug']: dct for dct in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
