import pygame
import time

# 색 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# 초기화
pygame.init()
pygame.mixer.init()

# 화면 초기 설정
Screen_Horizon = 1920
w = Screen_Horizon
Screen_Vertical = 1080
h = Screen_Vertical

Screen = pygame.display.set_mode((Screen_Horizon, Screen_Vertical))

# 화면 타이틀 설정
pygame.display.set_caption("TEMP")

# FPS
clock = pygame.time.Clock()

# 배경화면 불러오기
img_Background = pygame.image.load('Start_Select_BG.jpg')

# 스프라이트 불러오기

    #노트 입력 마커
img_Note_Press = pygame.image.load(r'NOTE\Note_Press.png')

    #판정 이미지
img_Judge_PGREAT = pygame.image.load(r'JUDGE\Judge_100+.png')
img_Judge_GREAT = pygame.image.load(r'JUDGE\Judge_100.png')
img_Judge_GOOD = pygame.image.load(r'JUDGE\Judge_50.png')
img_Judge_MISS = pygame.image.load(r'JUDGE\Judge_Miss.png')

    #메인화면 옵션 이미지
img_main_Start = pygame.image.load(r'MAIN\START.png')
img_main_Option = pygame.image.load(r'MAIN\OPTION.png')
img_main_Exit = pygame.image.load(r'MAIN\EXIT.png')

    #커서 이미지
img_main_Cursor = pygame.image.load(r'CURSOR\CURSOR.png')
img_option_Cursor = pygame.image.load(r'CURSOR\CURSOR.png')
    # 출처 : https://www.flaticon.com/kr/free-icons/mouse-cursor

    #가이드 이미지
img_main_Guide = pygame.image.load(r'MAIN\MAIN_GUIDE.png')

    #곡 자켓 이미지
img_Song_jacket = [
                pygame.image.load(r'SONG_JACKET\Select_Song_img_SONG1.png'), 
                pygame.image.load(r'SONG_JACKET\Select_Song_img_SONG2.png'),
                pygame.image.load(r'SONG_JACKET\Select_Song_img_SONG3.png')
                ]

img_Song_jacket_Size = img_Song_jacket[0].get_rect().size
img_Song_jacket_Horizon = img_Song_jacket_Size[0]
img_Song_jacket_Vertical = img_Song_jacket_Size[1]

# 폰트 정의
Combo_Font = pygame.font.Font(None, 100)
Back_Font = pygame.font.Font(None, 100)
Early_Late_Font = pygame.font.Font(None, 50)


# 메인 선택옵션 사이즈 구하기
img_main_Start_Size = img_main_Start.get_rect().size
img_main_Start_Horizon = img_main_Start_Size[0]
img_main_Start_Vertical = img_main_Start_Size[1]

img_main_Option_Size = img_main_Option.get_rect().size
img_main_Option_Horizon = img_main_Start_Size[0]
img_main_Option_Vertical = img_main_Start_Size[1]

img_main_Exit_Size = img_main_Exit.get_rect().size
img_main_Exit_Horizon = img_main_Exit_Size[0]
img_main_Exit_Vertical = img_main_Exit_Size[1]

#메인 가이드 사이즈 구하기
img_main_Guide_Size = img_main_Guide.get_rect().size
img_main_Guide_Horizon = img_main_Guide_Size[0]
img_main_Guide_Vertical = img_main_Guide_Size[1]

# 판정 이미지 사이즈 구하기
img_Judge_PGREAT_Size = img_Judge_PGREAT.get_rect().size
img_Judge_GREAT_Size = img_Judge_GREAT.get_rect().size
img_Judge_GOOD_Size = img_Judge_GOOD.get_rect().size
img_Judge_MISS_Size = img_Judge_MISS.get_rect().size

img_Judge_Vertical = img_Judge_PGREAT_Size[1]

img_Judge_PGREAT_Horizon = img_Judge_PGREAT_Size[0]
img_Judge_GREAT_Horizon = img_Judge_GREAT_Size[0]
img_Judge_GOOD_Horizon = img_Judge_GOOD_Size[0]
img_Judge_MISS_Horizon = img_Judge_MISS_Size[0]

# 노트 사이즈 구하기
img_Note_Press_Size = img_Note_Press.get_rect().size
img_Note_Press_Horizon = img_Note_Press_Size[0]
img_Note_Press_Vertical = img_Note_Press_Size[1]

# 노트 터치이미지 좌표 찍기
img_Note_Press_1_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_1_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2


img_Note_Press_2_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_2_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_3_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_3_Y_Pos = h/2 + h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_4_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_4_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_5_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_5_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_6_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_6_Y_Pos = h/2 - img_Note_Press_Vertical/2

img_Note_Press_7_X_Pos = w/2 - w/10 - img_Note_Press_Horizon/2
img_Note_Press_7_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_8_X_Pos = w/2 - img_Note_Press_Horizon/2
img_Note_Press_8_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

img_Note_Press_9_X_Pos = w/2 + w/10 - img_Note_Press_Horizon/2
img_Note_Press_9_Y_Pos = h/2 - h/5.625 - img_Note_Press_Vertical/2

# 키입력 감지
key_Press = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 노트 출력 애니메이션
Note_Now = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Note_Anime = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Note_Speed = 0.5

# 인게임 시스템
    #JUDGE
judge_array = [0, 0, 0, 0]
judge_100p = 25
judge_100 = 50
judge_50 = 150
judge_print = -1
judge_frame = 0

combo = 0

Early_Late = -1

Option_Current_Page = 0
All_Page = 2 - 1
Change_Page = 0

    #OPTION
Note_Color = GREEN
Current_Note_Color = 1

Hit_Sound_Volume = 1
Effect_Volume = 1

Effect_Sound = pygame.mixer.Sound(r'Sound\Effect.mp3')
Select_Sound = pygame.mixer.Sound(r'Sound\Select.mp3')

Hit_Sound_Array = [
            pygame.mixer.Sound(r'Sound\Hit_Sound_1.wav'),
            pygame.mixer.Sound(r'Sound\Hit_Sound_2.mp3'),
            pygame.mixer.Sound(r'Sound\Hit_Sound_3.ogg')
            ]

Hit_Sound_Name = [
            'Stick',
            'Drum',
            'Clap'
            ]

Current_Hit_Sound = 0
All_Hit_Sound = 3 - 1

Hit_Sound = pygame.mixer.Sound(Hit_Sound_Array[Current_Hit_Sound])

    #COLOR
Note_Frame_Color = YELLOW
Current_Note_Frame_Color = 3

Color_Array = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
Color_Array_Size = 6 - 1

    #JACKET
Current_jacket = 0
jacket_Size = 3 - 1
jacket_LEFT_Pos = (-img_Song_jacket_Horizon/2, h/2 + h/16 - img_Song_jacket_Vertical/2)
jacket_CENTER_Pos = (w/2 - img_Song_jacket_Horizon/2, h/2 - img_Song_jacket_Vertical/2)
jacket_RIGHT_Pos = (w - img_Song_jacket_Horizon/2, h/2 + h/16 - img_Song_jacket_Vertical/2)

jacket_Name = [
                'Song1',
                'Song2',
                'Song3'
                ]

    #PLAYING NOW
Current_Play_Song = ''


# 판정 카운트
def judge_count(j):

    global combo

    if j == 'PGREAT':
        judge_array[0] += 1
        combo += 1
        return 0
    elif j == 'GREAT':
        judge_array[1] += 1
        combo += 1
        return 1
    elif j == 'GOOD':
        judge_array[2] += 1
        combo += 1
        return 2
    elif j == 'MISS':
        judge_array[3] += 1
        combo =0
        return 3
    
def judge(Note_Num):

    global Early_Late

    if Note_Anime[Note_Num] >= 10 - ((10 / (Note_Speed * fps)) * (judge_100p / 10)) and Note_Anime[Note_Num] <= 10 + ((10 / (Note_Speed * fps)) * (judge_100p / 10)):
        Note_Now[Note_Num] = 0
        Note_Anime[Note_Num] = 0
        return judge_count('PGREAT')
    
    if Note_Anime[Note_Num] < 10 - ((10 / (Note_Speed * fps)) * (judge_100p / 10)) and Note_Anime[Note_Num] >= 10 - ((10 / (Note_Speed * fps)) * (judge_100 / 10)):
        Note_Now[Note_Num] = 0
        Note_Anime[Note_Num] = 0
        Early_Late = 1
        return judge_count('GREAT')
    if Note_Anime[Note_Num] > 10 + ((10 / (Note_Speed * fps)) * (judge_100p / 10)) and Note_Anime[Note_Num] <= 10 + ((10 / (Note_Speed * fps)) * (judge_100 / 10)):
        Note_Now[Note_Num] = 0
        Note_Anime[Note_Num] = 0
        Early_Late = 0
        return judge_count('GREAT')

    if Note_Anime[Note_Num] < 10 - ((10 / (Note_Speed * fps)) * (judge_100 / 10)) and Note_Anime[Note_Num] >= 10 - ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
        Note_Now[Note_Num] = 0
        Note_Anime[Note_Num] = 0
        Early_Late = 1
        return judge_count('GOOD')
    if Note_Anime[Note_Num] > 10 + ((10 / (Note_Speed * fps)) * (judge_100 / 10)) and Note_Anime[Note_Num] <= 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
        Note_Now[Note_Num] = 0
        Note_Anime[Note_Num] = 0
        Early_Late = 0
        return judge_count('GOOD')
    
    Early_Late = -1
    return judge_print


#커서 세팅
Main_Cursor_Pos = (w/2 - w/4.5, h/2 - img_main_Start_Vertical * 2.5)
Main_Cursor_Current = 'START'

Option_Cursor_Pos = (w - w/4, h/2 - h/4)
Option_Cursor_Current = 'NOTE_SPEED'



#이벤트 루프
IsRunning = True
Window = 'Main'

while IsRunning:
    #Frame Per Second
    fps = 200
    dt = clock.tick(fps)

    if Window == 'Main':

        #Set BG
        Screen.blit(img_Background, (0, 0))
        Screen.blit(img_main_Start, (w/36, h/2 - img_main_Start_Vertical*2.5))
        Screen.blit(img_main_Option, (w/36, h/2))
        Screen.blit(img_main_Exit, (w/36, h/2 + img_main_Exit_Vertical*2.5))
        Screen.blit(img_main_Guide, (w - img_main_Guide_Horizon, h - img_main_Guide_Vertical))
        Screen.blit(img_main_Cursor, Main_Cursor_Pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False

            IsPressed_Arrow = 0

            #KEYDOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Effect_Sound.play()

                    if Main_Cursor_Current == 'START' and IsPressed_Arrow == 0:
                        Main_Cursor_Pos = (w/2 - w/4.5, h/2)
                        Main_Cursor_Current = 'OPTION'
                        IsPressed_Arrow = 1

                    if Main_Cursor_Current == 'OPTION' and IsPressed_Arrow == 0:
                        Main_Cursor_Pos = (w/2 - w/4.5, h/2 + img_main_Exit_Vertical*2.5)
                        Main_Cursor_Current = 'EXIT'
                        IsPressed_Arrow = 1

                if event.key == pygame.K_UP:
                    Effect_Sound.play()

                    if Main_Cursor_Current == 'EXIT' and IsPressed_Arrow == 0:
                        Main_Cursor_Pos = (w/2 - w/4.5, h/2)
                        Main_Cursor_Current = 'OPTION'
                        IsPressed_Arrow = 1

                    if Main_Cursor_Current == 'OPTION' and IsPressed_Arrow == 0:
                        Main_Cursor_Pos = (w/2 - w/4.5, h/2 - img_main_Start_Vertical*2.5)
                        Main_Cursor_Current = 'START'
                        IsPressed_Arrow = 1

                if event.key == pygame.K_SPACE:
                    Select_Sound.play()

                    if Main_Cursor_Current == 'START':
                        Window = 'Select_Song'

                    if Main_Cursor_Current == 'OPTION':
                        Window = 'Option'

                    if Main_Cursor_Current == 'EXIT':
                        IsRunning = False

            #KEYUP
            if event.type == pygame.KEYUP:
                pass


    if Window == 'Option':

        #Font Render
        View_Page = Combo_Font.render(str("-- %d / %d --" %((Option_Current_Page+1), (All_Page+1))), True, BLACK)
        View_Page_Size = View_Page.get_size()
        View_Page_Horizon = View_Page_Size[0]
        View_Page_Vertical = View_Page_Size[1]
        
        #Set BG
        Screen.blit(img_Background, (0, 0))
        Screen.blit(img_main_Option, (w/2 - img_main_Option_Horizon/1.7, img_main_Option_Vertical/4))
        Screen.blit(img_main_Cursor, Option_Cursor_Pos)
        Screen.blit(View_Page, (w/2 - View_Page_Horizon/2, h - View_Page_Vertical))
        
        #Font Render
        Button_Back = Back_Font.render(str("BACK = ESC"), True, BLACK)
        Setting_Guide = Back_Font.render(str("CONTROL : ARROW"), True, BLACK)

        #Font Write
        Screen.blit(Button_Back, (w/32, h - h/8))
        Screen.blit(Setting_Guide, (w - w/2 + w/8, h - h/8))

        if Option_Current_Page == 0:
            #Font Render
            Note_Speed_Font = Combo_Font.render(str("SPEED UP & DOWN 4 ~ 20  <- %d ->" %(25 - Note_Speed*20)), True, WHITE)
            Note_Frame_Color_Font = Combo_Font.render(str("NOTE FRAME COLOR"), True, Note_Frame_Color)
            Note_Color_Font = Combo_Font.render(str("NOTE COLOR"), True, Note_Color)

            #Font Write
            Screen.blit(Note_Speed_Font, (w/8, h/2 - h/4))
            Screen.blit(Note_Frame_Color_Font, (w/8, (h - h/4 + h/6)/2))
            Screen.blit(Note_Color_Font, (w/8, h/2 + h/6))

            #Draw Note Frame_Color / Color
            pygame.draw.rect(Screen, Note_Frame_Color, (w/2 + w/20, (h - h/4 + h/6)/2 - h/11.25, w/10, h/5.625), 10)
            pygame.draw.rect(Screen, Note_Color, (w/2 + w/20, h/2 + h/6 - h/11.25, w/10, h/5.625))

            if Change_Page == 1:
                Option_Cursor_Current = 'NOTE_SPEED'
                Option_Cursor_Pos = (w - w/4, h/2 - h/4)
                Change_Page = 0

        if Option_Current_Page == 1:
            #Font Render
            Hit_Sound_Font = Combo_Font.render(str("Hit Sound <- %s ->") %Hit_Sound_Name[Current_Hit_Sound], True, WHITE)
            Hit_Sound_Volume_Font = Combo_Font.render(str("Hit Sound Volume 0 ~ 10  <- %d ->" %(Hit_Sound_Volume * 10)), True, WHITE)
            Effect_Volume_Font = Combo_Font.render(str("Effect Volume 0 ~ 10  <- %d ->" %(Effect_Volume * 10)), True, WHITE)

            #Font Write
            Screen.blit(Hit_Sound_Font, (w/8, h/2 - h/4))
            Screen.blit(Hit_Sound_Volume_Font, (w/8, h/2 + h/6))
            Screen.blit(Effect_Volume_Font, (w/8, (h - h/4 + h/6)/2))

            if Change_Page == 1:
                Option_Cursor_Current = 'HIT_SOUND'
                Option_Cursor_Pos = (w - w/4, h/2 - h/4)
                Change_Page = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
            
            IsPressed_Arrow = 0

            #KEYDOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Select_Sound.play()
                    Window = 'Main'
                
                if event.key == pygame.K_SPACE:
                    Select_Sound.play()
                    if Option_Current_Page >= All_Page:
                        Option_Current_Page = 0
                    else:
                        Option_Current_Page += 1
                    Change_Page = 1
                    IsPressed_Arrow = 1

                if Option_Current_Page == 0:
                    if event.key == pygame.K_DOWN:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, (h - h/4 + h/6)/2)
                            Option_Cursor_Current = 'NOTE_FRAME_COLOR'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME_COLOR' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, h/2 + h/6)
                            Option_Cursor_Current = 'NOTE_COLOR'
                            IsPressed_Arrow = 1
    
                    if event.key == pygame.K_UP:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, (h - h/4 + h/6)/2)
                            Option_Cursor_Current = 'NOTE_FRAME_COLOR'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME_COLOR' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, h/2 - h/4)
                            Option_Cursor_Current = 'NOTE_SPEED'
                            IsPressed_Arrow = 1

                    if event.key == pygame.K_LEFT:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0 and Note_Speed < 1:
                            Note_Speed += 0.05
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_FRAME_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Frame_Color <= 0:
                                Current_Note_Frame_Color = Color_Array_Size
                                Note_Frame_Color = Color_Array[Current_Note_Frame_Color]
                                IsPressed_Arrow = 1
                            else:
                                Current_Note_Frame_Color -= 1
                                Note_Frame_Color = Color_Array[Current_Note_Frame_Color]
                                IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Color <= 0:
                                Current_Note_Color = Color_Array_Size
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1
                            else:
                                Current_Note_Color -= 1
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1
                            
                    if event.key == pygame.K_RIGHT:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'NOTE_SPEED' and IsPressed_Arrow == 0 and Note_Speed > 0.26:
                            Note_Speed -= 0.05
                            IsPressed_Arrow = 1
                                    
                        if Option_Cursor_Current == 'NOTE_FRAME_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Frame_Color >= Color_Array_Size:
                                Current_Note_Frame_Color = 0
                                Note_Frame_Color = Color_Array[Current_Note_Frame_Color]
                                IsPressed_Arrow = 1
                            else:
                                Current_Note_Frame_Color += 1
                                Note_Frame_Color = Color_Array[Current_Note_Frame_Color]
                                IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'NOTE_COLOR' and IsPressed_Arrow == 0:
                            if Current_Note_Color >= Color_Array_Size:
                                Current_Note_Color = 0
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1
                            else:
                                Current_Note_Color += 1
                                Note_Color = Color_Array[Current_Note_Color]
                                IsPressed_Arrow = 1

                if Option_Current_Page == 1:
                    if event.key == pygame.K_DOWN:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, (h - h/4 + h/6)/2)
                            Option_Cursor_Current = 'EFFECT_VOLUME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, h/2 + h/6)
                            Option_Cursor_Current = 'HIT_SOUND_VOLUME'
                            IsPressed_Arrow = 1
    
                    if event.key == pygame.K_UP:

                        Effect_Sound.play()

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, (h - h/4 + h/6)/2)
                            Option_Cursor_Current = 'EFFECT_VOLUME'
                            IsPressed_Arrow = 1

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:
                            Option_Cursor_Pos = (w - w/4, h/2 - h/4)
                            Option_Cursor_Current = 'HIT_SOUND'
                            IsPressed_Arrow = 1

                    if event.key == pygame.K_LEFT:

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:

                            if Current_Hit_Sound > 0:
                                Current_Hit_Sound -= 1
                                Hit_Sound = Hit_Sound_Array[Current_Hit_Sound]

                            IsPressed_Arrow = 1

                            Hit_Sound.play()

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:

                            if Effect_Volume >= 0.1:
                                Effect_Volume -= 0.1
                                Effect_Sound.set_volume(Effect_Volume)
                                IsPressed_Arrow = 1

                            Effect_Sound.play()

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:

                            if Hit_Sound_Volume >= 0.1:
                                Hit_Sound_Volume -= 0.1
                                Hit_Sound.set_volume(Hit_Sound_Volume)
                                IsPressed_Arrow = 1

                            Hit_Sound.play()

                    if event.key == pygame.K_RIGHT:

                        if Option_Cursor_Current == 'HIT_SOUND' and IsPressed_Arrow == 0:

                            if Current_Hit_Sound < All_Hit_Sound:
                                Current_Hit_Sound += 1
                                Hit_Sound = Hit_Sound_Array[Current_Hit_Sound]

                            IsPressed_Arrow = 1

                            Hit_Sound.set_volume(Hit_Sound_Volume)
                            Hit_Sound.play()

                        if Option_Cursor_Current == 'EFFECT_VOLUME' and IsPressed_Arrow == 0:

                            if Effect_Volume <= 0.9:
                                Effect_Volume += 0.1
                                Effect_Sound.set_volume(Effect_Volume)
                                IsPressed_Arrow = 1

                            Effect_Sound.play()

                        if Option_Cursor_Current == 'HIT_SOUND_VOLUME' and IsPressed_Arrow == 0:

                            if Hit_Sound_Volume <= 0.9:
                                Hit_Sound_Volume += 0.1
                                Hit_Sound.set_volume(Hit_Sound_Volume)
                                IsPressed_Arrow = 1

                            Hit_Sound.play()



            if event.type == pygame.KEYUP:
                pass


    if Window == 'Select_Song':

        #Set BG
        Screen.blit(img_Background, (0, 0))

        #Draw Jacket
        Screen.blit(img_Song_jacket[Current_jacket],jacket_CENTER_Pos)
        if Current_jacket >= jacket_Size:
            Screen.blit(img_Song_jacket[Current_jacket-1], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[0], jacket_RIGHT_Pos)
        elif Current_jacket <= 0:
            Screen.blit(img_Song_jacket[jacket_Size], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[Current_jacket+1], jacket_RIGHT_Pos)
        else:
            Screen.blit(img_Song_jacket[Current_jacket-1], jacket_LEFT_Pos)
            Screen.blit(img_Song_jacket[Current_jacket+1], jacket_RIGHT_Pos)
        
        #Set Font
        Button_Back = Back_Font.render(str("BACK = ESC"), True, BLACK)
        Font_Song_Select = Combo_Font.render(str("SELECT SONG"), True, WHITE)
        Font_Song_Name = Combo_Font.render(str("%s" %jacket_Name[Current_jacket]), True, WHITE)

        #Get Song Name Font Size
        Font_Song_Name_Size = Font_Song_Name.get_size()
        Font_Song_Name_Horizon = Font_Song_Name_Size[0]
        Font_Song_Name_Vertical = Font_Song_Name_Size[1]

        #Write Font
        Screen.blit(Button_Back, (w/32, h - h/8))
        Screen.blit(Font_Song_Select, (w/2 - w/8, h/100))
        Screen.blit(Font_Song_Name, (w/2 - Font_Song_Name_Horizon/2, h/2 + h/4 + Font_Song_Name_Vertical/2))


        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    Select_Sound.play()
                    Window = 'Main'

                if event.key == pygame.K_LEFT:

                    Effect_Sound.play()

                    if Current_jacket <= 0:
                        Current_jacket = jacket_Size
                    else:
                        Current_jacket -= 1

                if event.key == pygame.K_RIGHT:
                    
                    Effect_Sound.play()

                    if Current_jacket >= jacket_Size:
                        Current_jacket = 0
                    else:
                        Current_jacket += 1
                
                if event.key == pygame.K_SPACE:

                    Select_Sound.play()

                    if Current_jacket == 0:
                        Current_Play_Song = jacket_Name[Current_jacket]
                        Window = 'InGame'
                        
            
            if event.type == pygame.KEYUP:
                pass


    if Window == 'InGame':

        if judge_print != -1:
            judge_frame += 1
            if judge_frame >= 100:
                judge_print = -1

                if Early_Late != -1:
                    Early_Late = -1

                judge_frame = 0

        #Set BG
        Screen.blit(img_Background, (0, 0))

        #Draw Combo
        View_Combo = Combo_Font.render(str(combo), True, WHITE)
        View_Combo_Size = View_Combo.get_size()
        View_Combo_Horizon = View_Combo_Size[0]

        Screen.blit(View_Combo, (w/2 - View_Combo_Horizon/2, h - h/8))

        #Draw Note Frame
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/10 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625), 10) #1
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625), 10) #2
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 + w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625), 10) #3
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/10 - w/20, h/2 - h/11.25, w/10, h/5.625), 10) #4
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/20, h/2 - h/11.25, w/10, h/5.625), 10) #5
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 + w/20, h/2 - h/11.25, w/10, h/5.625), 10) #6
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/10 - w/20, h/2 + h/11.25, w/10, h/5.625), 10) #7
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 - w/20, h/2 + h/11.25, w/10, h/5.625), 10) #8
        pygame.draw.rect(Screen, Note_Frame_Color, (w/2 + w/20, h/2 + h/11.25, w/10, h/5.625), 10) #9

        #Draw Side Line
        pygame.draw.line(Screen, CYAN, [w/2 - w/3, 0], [w/2 - w/3, h], 10)
        pygame.draw.line(Screen, MAGENTA, [w/2 + w/3, 0], [w/2 + w/3, h], 10)

        #Note Spawn
        if Note_Now[0] == 1:
            if Note_Anime[0] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[0] = 0
                Note_Anime[0] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[0] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - (w/100 * Note_Anime[0])/2, h/2 + h/5.625 - (h/56.25 * Note_Anime[0])/2, w/100 * Note_Anime[0], h/56.25 * Note_Anime[0]))
            if Note_Anime[0] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[0] += (10 / (Note_Speed * fps))
            
        if Note_Now[1] == 1:
            if Note_Anime[1] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[1] = 0
                Note_Anime[1] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[1] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - (w/100 * Note_Anime[1])/2, h/2 + h/5.625 - (h/56.25 * Note_Anime[1])/2, w/100 * Note_Anime[1], h/56.25 * Note_Anime[1]))
            if Note_Anime[1] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[1] += (10 / (Note_Speed * fps))
            
        if Note_Now[2] == 1:
            if Note_Anime[2] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[2] = 0
                Note_Anime[2] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[2] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - (w/100 * Note_Anime[2])/2, h/2 +h/5.625 - (h/56.25 * Note_Anime[2])/2, w/100 * Note_Anime[2], h/56.25 * Note_Anime[2]))
            if Note_Anime[2] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 + h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[2] += (10 / (Note_Speed * fps))

        if Note_Now[3] == 1:
            if Note_Anime[3] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[3] = 0
                Note_Anime[3] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[3] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - (w/100 * Note_Anime[3])/2, h/2 - (h/56.25 * Note_Anime[3])/2, w/100 * Note_Anime[3], h/56.25 * Note_Anime[3]))
            if Note_Anime[3] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 - h/11.25, w/10, h/5.625))
            Note_Anime[3] += (10 / (Note_Speed * fps))

        if Note_Now[4] == 1:
            if Note_Anime[4] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[4] = 0
                Note_Anime[4] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[4] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - (w/100 * Note_Anime[4])/2, h/2 - (h/56.25 * Note_Anime[4])/2, w/100 * Note_Anime[4], h/56.25 * Note_Anime[4]))
            if Note_Anime[4] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 - h/11.25, w/10, h/5.625))
            Note_Anime[4] += (10 / (Note_Speed * fps))

        if Note_Now[5] == 1:
            if Note_Anime[5] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[5] = 0
                Note_Anime[5] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[5] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - (w/100 * Note_Anime[5])/2, h/2 - (h/56.25 * Note_Anime[5])/2, w/100 * Note_Anime[5], h/56.25 * Note_Anime[5]))
            if Note_Anime[5] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 - h/11.25, w/10, h/5.625))
            Note_Anime[5] += (10 / (Note_Speed * fps))

        if Note_Now[6] == 1:
            if Note_Anime[6] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[6] = 0
                Note_Anime[6] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[6] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - (w/100 * Note_Anime[6])/2, h/2 - h/5.625 - (h/56.25 * Note_Anime[6])/2, w/100 * Note_Anime[6], h/56.25 * Note_Anime[6]))
            if Note_Anime[6] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/10 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[6] += (10 / (Note_Speed * fps))

        if Note_Now[7] == 1:
            if Note_Anime[7] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[7] = 0
                Note_Anime[7] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[7] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - (w/100 * Note_Anime[7])/2, h/2 - h/5.625 - (h/56.25 * Note_Anime[7])/2, w/100 * Note_Anime[7], h/56.25 * Note_Anime[7]))
            if Note_Anime[7] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[7] += (10 / (Note_Speed * fps))

        if Note_Now[8] == 1:
            if Note_Anime[8] > 10 + ((10 / (Note_Speed * fps)) * (judge_50 / 10)):
                Note_Now[8] = 0
                Note_Anime[8] = 0
                judge_print = judge_count('MISS')
                combo = 0
            if Note_Anime[8] <= 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - (w/100 * Note_Anime[8])/2, h/2 - h/5.625 - (h/56.25 * Note_Anime[8])/2, w/100 * Note_Anime[8], h/56.25 * Note_Anime[8]))
            if Note_Anime[8] > 10:
                pygame.draw.rect(Screen, Note_Color, (w/2 + w/10 - w/20, h/2 - h/5.625 - h/11.25, w/10, h/5.625))
            Note_Anime[8] += (10 / (Note_Speed * fps))

        #Draw Note Press
        if key_Press[0] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_1_X_Pos, img_Note_Press_1_Y_Pos))
        if key_Press[1] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_2_X_Pos, img_Note_Press_2_Y_Pos))
        if key_Press[2] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_3_X_Pos, img_Note_Press_3_Y_Pos))
        if key_Press[3] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_4_X_Pos, img_Note_Press_4_Y_Pos))
        if key_Press[4] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_5_X_Pos, img_Note_Press_5_Y_Pos))
        if key_Press[5] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_6_X_Pos, img_Note_Press_6_Y_Pos))
        if key_Press[6] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_7_X_Pos, img_Note_Press_7_Y_Pos))
        if key_Press[7] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_8_X_Pos, img_Note_Press_8_Y_Pos))
        if key_Press[8] == 1:
            Screen.blit(img_Note_Press, (img_Note_Press_9_X_Pos, img_Note_Press_9_Y_Pos))

        #Draw Judge
        if judge_print == 0:
            Screen.blit(img_Judge_PGREAT, (w/2 - img_Judge_PGREAT_Horizon/2 , img_Judge_Vertical/2))

        if judge_print == 1:
            Screen.blit(img_Judge_GREAT, (w/2 - img_Judge_GREAT_Horizon/2 , img_Judge_Vertical/2))
            
            if Early_Late == 0:
                Font_Early_Late = Early_Late_Font.render(str("LATE"), True, MAGENTA)
                Screen.blit(Font_Early_Late, (w/2 + img_Judge_PGREAT_Horizon, img_Judge_Vertical/2 + h/32))

            elif Early_Late == 1:
                Font_Early_Late = Early_Late_Font.render(str("EARLY"), True, CYAN)
                Screen.blit(Font_Early_Late, (w/2 - img_Judge_PGREAT_Horizon - w/20, img_Judge_Vertical/2 + h/32))

        if judge_print == 2:
            Screen.blit(img_Judge_GOOD, (w/2 - img_Judge_GOOD_Horizon/2 , img_Judge_Vertical/2))
            
            if Early_Late == 0:
                Font_Early_Late = Early_Late_Font.render(str("LATE"), True, MAGENTA)
                Screen.blit(Font_Early_Late, (w/2 + img_Judge_PGREAT_Horizon, img_Judge_Vertical/2 + h/32))

            elif Early_Late == 1:
                Font_Early_Late = Early_Late_Font.render(str("EARLY"), True, CYAN)
                Screen.blit(Font_Early_Late, (w/2 - img_Judge_PGREAT_Horizon - w/20, img_Judge_Vertical/2 + h/32))

        if judge_print == 3:
            Screen.blit(img_Judge_MISS, (w/2 - img_Judge_MISS_Horizon/2 , img_Judge_Vertical/2))
            
            if Early_Late == 0:
                Font_Early_Late = Early_Late_Font.render(str("LATE"), True, MAGENTA)
                Screen.blit(Font_Early_Late, (w/2 + img_Judge_PGREAT_Horizon, img_Judge_Vertical/2 + h/32))

            elif Early_Late == 1:
                Font_Early_Late = Early_Late_Font.render(str("EARLY"), True, CYAN)
                Screen.blit(Font_Early_Late, (w/2 - img_Judge_PGREAT_Horizon - w/20, img_Judge_Vertical/2 + h/32))

        if judge_print == -1:
            pygame.display.flip()


        #Check EVENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #QUIT GAME
                IsRunning = False
            
            #KEYDOWN
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    Select_Sound.play()
                    Window = 'Select_Song'

                if event.key != pygame.K_ESCAPE:

                    Hit_Sound.play()

                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        key_Press[0] = 1
                        judge_print = judge(0)
                            
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        key_Press[1] = 1
                        judge_print = judge(1)

                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        key_Press[2] = 1
                        judge_print = judge(2)

                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        key_Press[3] = 1
                        judge_print = judge(3)

                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        key_Press[4] = 1
                        judge_print = judge(4)

                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        key_Press[5] = 1
                        judge_print = judge(5)

                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        key_Press[6] = 1
                        judge_print = judge(6)

                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        key_Press[7] = 1
                        judge_print = judge(7)

                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        key_Press[8] = 1
                        judge_print = judge(8)

                    if event.key == pygame.K_a:
                        Note_Now[0] = 1
                        Note_Now[1] = 1
                        Note_Now[2] = 1
                        Note_Now[3] = 1
                        Note_Now[4] = 1
                        Note_Now[5] = 1
                        Note_Now[6] = 1
                        Note_Now[7] = 1
                        Note_Now[8] = 1

            #KEYUP  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key_Press[0] = 0
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key_Press[1] = 0
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key_Press[2] = 0
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key_Press[3] = 0
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key_Press[4] = 0
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key_Press[5] = 0
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key_Press[6] = 0
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key_Press[7] = 0
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key_Press[8] = 0

    # Update Screen
    pygame.display.flip()


pygame.quit()