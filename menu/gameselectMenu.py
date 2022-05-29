from pickle import TRUE
from button import *
import pygame
import pygame_menu
from data.CharacterDataManager import *
from data.Stage import Stage
from data.StageDataManager import *
from game.StageGameplay import StageGame
from pygame_menu.utils import make_surface
from menu.CharacterSelectMenu import *
from pygame.locals import *
from data.Rank import Rank
from data.Defs import *
from menu.StageSelectMenu import *
from menu.LeaderBoardMenu import *
from menu.MypageMenu import *
from menu.CharacterSelectMenu import *
from menu.CharacterStoreMenu import *


class GameselectMenu:
    def __init__(self,screen):
        
        self.size = screen.get_size() 
        self.screen = screen
        self.changed_screen_size = self.screen.get_size()
        self.board_width=self.changed_screen_size[0] # x
        self.board_height=self.changed_screen_size[1] # y

        self.map1 = button(self.board_width, self.board_height, 0.2, 0.4, 0.2, 0.3, "Image/catthema/map1.png")
        self.map2 = button(self.board_width, self.board_height, 0.5, 0.4, 0.2, 0.3, "Image/catthema/map2.png")
        self.map3 = button(self.board_width, self.board_height, 0.8, 0.4, 0.2, 0.3, "Image/catthema/map3.png")

        self.level_map1 = button(self.board_width, self.board_height, 0.2, 0.6, 0.2, 0.05, "Image/catthema/LEVEL1.png")
        self.level_map2 = button(self.board_width, self.board_height, 0.5, 0.6, 0.2, 0.05, "Image/catthema/LEVEL1.png")
        self.level_map3 = button(self.board_width, self.board_height, 0.8, 0.6, 0.2, 0.05, "Image/catthema/LEVEL1.png")
        
        self.mode_map1 = button(self.board_width, self.board_height, 0.2, 0.6, 0.2, 0.05, "Image/catthema/EASY.png")
        self.mode_map2 = button(self.board_width, self.board_height, 0.5, 0.6, 0.2, 0.05, "Image/catthema/EASY.png")
        self.mode_map3 = button(self.board_width, self.board_height, 0.8, 0.6, 0.2, 0.05, "Image/catthema/EASY.png")

        self.rankpage = button(self.board_height,self.board_height,0.766,0.05,0.1,0.05,"Image/catthema/rank.png")
        self.mypage = button(self.board_height,self.board_height,0.5,0.05,0.1,0.05,"Image/catthema/mypage.png")
        self.gamemode = button(self.board_height,self.board_height,0.366,0.05,0.1,0.05,"Image/catthema/stage.png")
        self.store = button(self.board_height,self.board_height,0.233,0.05,0.1,0.05,"Image/catthema/store.png")
        self.setting = button(self.board_height,self.board_height,0.1,0.05,0.1,0.05,"Image/catthema/setting.png")
        self.logout= button(self.board_height,self.board_height,0.9,0.05,0.1,0.05,"Image/catthema/logout.png")
        self.help = button(self.board_height,self.board_height,0.633,0.05,0.1,0.05,"Image/catthema/help.png")

        self.barcol = button(self.board_height,self.board_height,0.5,0.0,1,0.2,"Image/catthema/bar.png")

        self.buttonlist1=[self.barcol,self.map1,self.map2,self.map3,self.level_map1,self.level_map2,self.level_map3,
        self.rankpage,self.mypage,self.gamemode,self.store,self.setting,self.logout,self.help] # stagemode

        self.buttonlist2=[self.barcol,self.map1,self.map2,self.map3,self.mode_map1,self.mode_map2,self.mode_map3,
        self.rankpage,self.mypage,self.gamemode,self.store,self.setting,self.logout,self.help] # inf mode

        self.attchar=["./Image/catthema/attack/cat_att.png","./Image/catthema/attack/dog.png","./Image/catthema/attack/snake.png"]

        self.stage_level_map1 = "1"
        self.stage_level_map2 = "1"
        self.stage_level_map3 = "1"

        self.inf_mode_map1 = 0
        self.inf_mode_map2 = 0
        self.inf_mode_map3 = 0

        self.mode = [("EASY",InfiniteGame.EasyMode()),("HARD",InfiniteGame.HardMode())]

        self.modestate="stage"

        self.temp1 = self.level_map1.image
        self.temp2 = self.level_map2.image
        self.temp3 = self.level_map3.image

        self.stage_data = StageDataManager.loadStageData() # 스테이지 데이터
        self.character_data = CharacterDataManager.load() # 캐릭터 데이터
        self.selectedChapter = [list(self.stage_data["chapter"].keys())[0]] 

        self.stay=0 

    def show(self,screen):     

        self.check_resize(screen)

        if self.modestate == "stage" : # stage mode

            screen.fill((255, 255, 255)) # 배경 나중에 바꾸기.

            for self.button in enumerate(self.buttonlist1): # 버튼 그리기
                self.button[1].change(screen.get_size()[0],screen.get_size()[1]) # 화면 사이즈 변경되면 버튼사이즈 바꿔줌.
                self.button[1].draw(screen,(0,0,0))

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos() # mouse

                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEMOTION: # 마우스모션

                    if self.map1.isOver(pos): # 이미지 바꿈
                        self.map1.image="Image/catthema/map1_dark.png"
                    else : self.map1.image="Image/catthema/map1.png" 
                    pygame.display.update()

                    if self.map2.isOver(pos):
                        self.map2.image="Image/catthema/map2_dark.png"
                    else : self.map2.image="Image/catthema/map2.png" 
                    pygame.display.update()

                    if self.map3.isOver(pos):
                        self.map3.image="Image/catthema/map3_dark.png"
                    else : self.map3.image="Image/catthema/map3.png" 
                    pygame.display.update()
                    
                    if self.level_map1.isOver(pos):
                        if self.stage_level_map1 == "1":
                            self.level_map1.image="Image/catthema/LEVEL2.png"
                        elif self.stage_level_map1 == "2":
                            self.level_map1.image="Image/catthema/LEVEL3.png"
                        elif self.stage_level_map1 == "3":
                            self.level_map1.image="Image/catthema/LEVEL1.png"
                    else : self.level_map1.image=self.temp1
                    pygame.display.update()

                    if self.level_map2.isOver(pos):
                        if self.stage_level_map2 == "1":
                            self.level_map2.image="Image/catthema/LEVEL2.png"
                        elif self.stage_level_map2 == "2":
                            self.level_map2.image="Image/catthema/LEVEL3.png"
                        elif self.stage_level_map2 == "3":
                            self.level_map2.image="Image/catthema/LEVEL1.png"
                    else : self.level_map2.image=self.temp2
                    pygame.display.update()

                    if self.level_map3.isOver(pos):
                        if self.stage_level_map3 == "1":
                            self.level_map3.image="Image/catthema/LEVEL2.png"
                        elif self.stage_level_map3 == "2":
                            self.level_map3.image="Image/catthema/LEVEL3.png"
                        elif self.stage_level_map3 == "3":
                            self.level_map3.image="Image/catthema/LEVEL1.png"
                    else : self.level_map3.image=self.temp3
                    pygame.display.update()

                    if self.gamemode.isOver(pos):
                        self.gamemode.image="Image/catthema/inf.png"
                    else : self.gamemode.image="Image/catthema/stage.png"
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭

                    if self.map1.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=Stage(self.stage_data["chapter"]["Dongguk university"][self.stage_level_map1])
                        StageGame(self.character_data,self.character_data[User.character],self.stage_map).main_info()
                    pygame.display.update()

                    if self.map2.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=Stage(self.stage_data["chapter"]["Night view"][self.stage_level_map2])
                        StageGame(self.character_data,self.character_data[User.character],self.stage_map).main_info()
                    pygame.display.update()

                    if self.map3.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=Stage(self.stage_data["chapter"]["Namsan"][self.stage_level_map3])
                        StageGame(self.character_data,self.character_data[User.character],self.stage_map).main_info()
                    pygame.display.update()

                    if self.level_map1.isOver(pos):
                        if self.stage_level_map1 == "1" :
                            self.temp1 = "Image/catthema/LEVEL2.png" # 이미지 바꾸기
                            self.stage_level_map1 = "2" # 바뀐 레벨로 저장.
                        
                        elif self.stage_level_map1 == "2" :
                            self.temp1 = "Image/catthema/LEVEL3.png" # 이미지 바꾸기
                            self.stage_level_map1 = "3" # 바뀐 레벨로 저장.
                        
                        elif self.stage_level_map1 == "3" :
                            self.temp1 = "Image/catthema/LEVEL1.png" # 이미지 바꾸기
                            self.stage_level_map1 = "1" # 바뀐 레벨로 저장.
                    pygame.display.update()

                    if self.level_map2.isOver(pos):
                        if self.stage_level_map2 == "1" :
                            self.temp2 = "Image/catthema/LEVEL2.png" # 이미지 바꾸기
                            self.stage_level_map2 = "2" # 바뀐 레벨로 저장.
                
                        elif self.stage_level_map2 == "2" :
                            self.temp2 = "Image/catthema/LEVEL3.png" # 이미지 바꾸기
                            self.stage_level_map2 = "3" # 바뀐 레벨로 저장.
                    
                        elif self.stage_level_map2 == "3" :
                            self.temp2 = "Image/catthema/LEVEL1.png" # 이미지 바꾸기
                            self.stage_level_map2 = "1" # 바뀐 레벨로 저장.
                    pygame.display.update()

                    if self.level_map3.isOver(pos):
                        if self.stage_level_map3 == "1" :
                            self.temp3 = "Image/catthema/LEVEL2.png" # 이미지 바꾸기
                            self.stage_level_map3 = "2" # 바뀐 레벨로 저장.

                        elif self.stage_level_map3 == "2" :
                            self.temp3 = "Image/catthema/LEVEL3.png" # 이미지 바꾸기
                            self.stage_level_map3 = "3" # 바뀐 레벨로 저장.

                        elif self.stage_level_map3 == "3" :
                            self.temp3 = "Image/catthema/LEVEL1.png" # 이미지 바꾸기
                            self.stage_level_map3 = "1" # 바뀐 레벨로 저장.
                    pygame.display.update()

                    if self.gamemode.isOver(pos):
                        self.gamemode.image="Image/catthema/inf.png"
                        self.modestate="inf"
                    pygame.display.update()

                    if self.mypage.isOver(pos):
                        Mypage(self.screen).show()

                    if self.rankpage.isOver(pos):
                        LeaderBoardMenu(self.screen).rank()

                    if self.store.isOver(pos):
                        CharacterStoreMenu(self.screen).show()

                    if self.help.isOver(pos):
                        HelpMenu(self.screen).show()

                    if self.logout.isOver(pos):
                        import Main 
                        Main.Login(self.screen).show()


        else :
            screen.fill((255, 255, 255)) # 배경 나중에 바꾸기.

            for self.button in enumerate(self.buttonlist2): # 버튼 그리기
                self.button[1].change(screen.get_size()[0],screen.get_size()[1]) # 화면 사이즈 변경되면 버튼사이즈 바꿔줌.
                self.button[1].draw(screen,(0,0,0))

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos() # mouse

                if event.type == pygame.QUIT:
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEMOTION: # 마우스모션

                    if self.map1.isOver(pos): # 이미지 바꿈
                        self.map1.image="Image/catthema/map1_dark.png"
                    else : self.map1.image="Image/catthema/map1.png" 
                    pygame.display.update()

                    if self.map2.isOver(pos):
                        self.map2.image="Image/catthema/map2_dark.png"
                    else : self.map2.image="Image/catthema/map2.png" 
                    pygame.display.update()

                    if self.map3.isOver(pos):
                        self.map3.image="Image/catthema/map3_dark.png"
                    else : self.map3.image="Image/catthema/map3.png" 
                    pygame.display.update()

                    if self.mode_map1.isOver(pos):
                        pygame.display.update()

                    if self.mode_map2.isOver(pos):
                        pygame.display.update()

                    if self.mode_map3.isOver(pos):
                        pygame.display.update()

                    if self.gamemode.isOver(pos):
                        self.gamemode.image="Image/catthema/stage.png"
                    else : self.gamemode.image="Image/catthema/inf.png"
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONUP: # 마우스 클릭

                    if self.map1.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=self.mode[self.inf_mode_map1][1]
                        InfiniteGame(self.character_data[User.character],self.stage_map,"Image/catthema/map1.png",self.attchar[0]).main()
                    pygame.display.update()

                    if self.map2.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=self.mode[self.inf_mode_map2][1]
                        InfiniteGame(self.character_data[User.character],self.stage_map,"Image/catthema/map2.png",self.attchar[1]).main()
                    pygame.display.update()

                    if self.map3.isOver(pos): # 맵 선택하면 게임이랑 연결시키기
                        self.stage_map=self.mode[self.inf_mode_map3][1]
                        InfiniteGame(self.character_data[User.character],self.stage_map,"Image/catthema/map3.png",self.attchar[2]).main()
                    pygame.display.update()

                    if self.mode_map1.isOver(pos):
                        if self.inf_mode_map1 == 0 :
                            self.inf_mode_map1 = 1
                            self.mode_map1.image="Image/catthema/HARD.png"
                        else :
                            self.inf_mode_map1 = 0
                            self.mode_map1.image="Image/catthema/EASY.png"
                    pygame.display.update()

                    if self.mode_map2.isOver(pos):
                        if self.inf_mode_map2 == 0 :
                            self.inf_mode_map2 = 1
                            self.mode_map2.image="Image/catthema/HARD.png"
                        else :
                            self.inf_mode_map2 = 0
                            self.mode_map2.image="Image/catthema/EASY.png"
                    pygame.display.update()

                    if self.mode_map3.isOver(pos):
                        if self.inf_mode_map3 == 0 :
                            self.inf_mode_map3 = 1
                            self.mode_map3.image="Image/catthema/HARD.png"
                        else :
                            self.inf_mode_map3 = 0
                            self.mode_map3.image="Image/catthema/EASY.png"
                    pygame.display.update()

                    if self.gamemode.isOver(pos):
                        self.gamemode.image="Image/catthema/stage.png"
                        self.modestate="stage"
                    pygame.display.update()

                    if self.mypage.isOver(pos):
                        Mypage(self.screen).show()

                    if self.rankpage.isOver(pos):
                        LeaderBoardMenu(self.screen).rank()

                    if self.store.isOver(pos):
                        CharacterStoreMenu(self.screen).show()

                    if self.help.isOver(pos):
                        HelpMenu(self.screen).show()

    # 화면 크기 조정 감지 및 비율 고정
    def check_resize(self,screen):
        if (self.size != screen.get_size()): #현재 사이즈와 저장된 사이즈 비교 후 다르면 변경
            changed_screen_size = self.screen.get_size() #변경된 사이즈
            ratio_screen_size = (changed_screen_size[0],changed_screen_size[0]*783/720) #y를 x에 비례적으로 계산
            if(ratio_screen_size[0]<320): #최소 x길이 제한
                ratio_screen_size = (494,537)
            if(ratio_screen_size[1]>783): #최대 y길이 제한
                ratio_screen_size = (720,783)
            screen = pygame.display.set_mode(ratio_screen_size,
                                                    pygame.RESIZABLE)
