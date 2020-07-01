# 텍스트를 이미지로 만들어서 훈련 데이터로 사용하기 위한 목적
from PIL import Image,ImageDraw,ImageFont

def HS_make_font(number,draw_text):
# 이미지로 출력할 글자 및 폰트 지정 (나눔고딕 트루타입폰트 파일)
    font = ImageFont.truetype("./Typo_SsangmunDongB.ttf", 25)

    # 이미지 사이즈 지정
    text_width = 28
    text_height = 28

    # 이미지 객체 생성 (배경 검정)
    canvas = Image.new('RGB', (text_width, text_height), "white")

    # 가운데에 그리기 (폰트 색: 하양)
    draw = ImageDraw.Draw(canvas)
    w, h = font.getsize(draw_text)
    draw.text(((text_width-w)/2.0,(text_height-h)/2.0), draw_text, 'black', font)

    # 가.png로 저장 및 출력해서 보기
    canvas.save(str(number)+'.png', "PNG")
    # canvas.show()




f = open('noblank_hangul.txt', 'r')
line_num = 1
line = f.readline()
while line:
    line = f.readline()
    for i in range(16):
        HS_make_font(line_num,line[i])
        line_num += 1


f.close()
