class master:
    def __init__(self,instances_list,saves_list,assets_list,disp_res_tupple,maxfps):
        self.instances_list=instances_list
        self.saves_list=saves_list
        self.assets_list=assets_list
        self.disp_res_tupple=disp_res_tupple
        self.maxfps=maxfps
    
    def init_instances(self):
        for instance in self.instances_list:
                if instance.is_just_created:
                     instance.create()
    def manage_instances(self):
        for instance in self.instances_list:
            instance.step()
    
    def draw_instances(self):
        for instance in self.instances_list:
            instance.draw()
    
    def game(self):
        import pygame
        pygame.init()
        screen=pygame.display.set_mode(self.disp_res_tupple)
        run=True
        clock=pygame.time.Clock()
        while run:
            self.init_instances()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.manage_instances()
            screen.fill((0,0,0))
            self.draw_instances()
            pygame.display.flip()
        clock.tick(self.maxfps)
        pygame.quit()

class adventure_field:
    is_just_created=True

    def __init__(self,map,instances):
        self.map=map
        self.instances=instances
    def create(self,master):
        master.instances_list.append(self.map,self.instances)
    def step(self,master):
        master.instances_list.append(self.map,self.instances)



