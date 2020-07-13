from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'video_id': 437255932},
        'instalacao-windows': {'titulo': 'Video Aperitivo: Instalação Windows', 'video_id': 437893110}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
