from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='437255932'),
    Video(slug='instalacao-windows', titulo='Video Aperitivo: Instalação Windows', vimeo_id='437893110')
]

# videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    videos = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'videos': videos})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
