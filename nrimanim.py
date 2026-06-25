from manim import *

class Scene_TheMath(Scene):
    def construct(self):
        
        # ==========================================================
        # PART 1A: RECIPROCAL INTUITION (Standard Spring)
        # ==========================================================
        
        title_recip = Text("Reciprocal (Standard Spring)", font_size=40, color=BLUE).to_edge(UP)
        
        # Create two nodes for reciprocal
        r_node1 = Dot(LEFT * 2, color=LIGHT_GREY, radius=0.2)
        r_node2 = Dot(RIGHT * 2, color=LIGHT_GREY, radius=0.2)
        r_label1 = Text("Node 1", font_size=24).next_to(r_node1, DOWN)
        r_label2 = Text("Node 2", font_size=24).next_to(r_node2, DOWN)
        r_spring = Line(r_node1.get_center(), r_node2.get_center(), color=GRAY)
        
        self.play(FadeIn(title_recip, r_node1, r_node2, r_label1, r_label2, r_spring))
        self.wait(1)
        
        # Reciprocal Action 1: Displace Node 1
        r_disp1 = Arrow(r_node1.get_center(), r_node1.get_center() + RIGHT*0.5, color=YELLOW, buff=0)
        r_force2 = Arrow(r_node2.get_center(), r_node2.get_center() + RIGHT*1.5, color=BLUE, buff=0)
        r_f2_label = MathTex(r"+k^e \Delta_1", color=BLUE).next_to(r_force2, UP)
        
        self.play(GrowArrow(r_disp1))
        self.play(GrowArrow(r_force2), Write(r_f2_label))
        self.wait(1)
        self.play(FadeOut(r_disp1, r_force2, r_f2_label))
        
        # Reciprocal Action 2: Displace Node 2 (Symmetric Reaction)
        r_disp2 = Arrow(r_node2.get_center(), r_node2.get_center() + RIGHT*0.5, color=YELLOW, buff=0)
        r_force1 = Arrow(r_node1.get_center(), r_node1.get_center() + RIGHT*1.5, color=BLUE, buff=0)
        r_f1_label = MathTex(r"+k^e \Delta_2", color=BLUE).next_to(r_force1, UP)
        
        self.play(GrowArrow(r_disp2))
        self.play(GrowArrow(r_force1), Write(r_f1_label))
        self.wait(2)
        
        # Clear screen for Non-Reciprocal
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # ==========================================================
        # PART 1B: NON-RECIPROCAL INTUITION (Active Spring)
        # ==========================================================
        
        title_nonrecip = Text("Non-Reciprocal (Active Spring)", font_size=40, color=ORANGE).to_edge(UP)
        
        node1 = Dot(LEFT * 2, color=BLUE, radius=0.2)
        node2 = Dot(RIGHT * 2, color=BLUE, radius=0.2)
        label1 = Text("Node 1", font_size=24).next_to(node1, DOWN)
        label2 = Text("Node 2", font_size=24).next_to(node2, DOWN)
        spring = Line(node1.get_center(), node2.get_center(), color=ORANGE)
        
        self.play(FadeIn(title_nonrecip, node1, node2, label1, label2, spring))
        self.wait(1)
        
        # Action 1: Displace Node 1
        disp1 = Arrow(node1.get_center(), node1.get_center() + RIGHT*0.5, color=YELLOW, buff=0)
        force2 = Arrow(node2.get_center(), node2.get_center() + RIGHT*1.5, color=GREEN, buff=0)
        f2_label = MathTex(r"+k^o \Delta_1", color=GREEN).next_to(force2, UP)
        
        self.play(GrowArrow(disp1))
        self.play(GrowArrow(force2), Write(f2_label))
        self.wait(1)
        self.play(FadeOut(disp1, force2, f2_label))
        
        # Action 2: Displace Node 2 (Asymmetric/Opposite Reaction)
        disp2 = Arrow(node2.get_center(), node2.get_center() + RIGHT*0.5, color=YELLOW, buff=0)
        force1 = Arrow(node1.get_center(), node1.get_center() + LEFT*1.5, color=RED, buff=0)
        f1_label = MathTex(r"-k^o \Delta_2", color=RED).next_to(force1, UP)
        
        self.play(GrowArrow(disp2))
        self.play(GrowArrow(force1), Write(f1_label))
        self.wait(2)
        

       
        self.play(FadeOut(node1, node2, label1, label2, spring, disp2, force1, f1_label))
        
        
        matrix_title = Text("We can model this interaction with the following matrix", font_size=22, color=BLUE).to_edge(UP, buff=2.0)
        
        
        self.play(Write(matrix_title))
        
        
        matrix_eq = MathTex(
            r"\begin{pmatrix} F_{1} \\ F_{2} \end{pmatrix} = ",
            r"\begin{pmatrix} 0 & ", r"+k^{o}", r" \\ ", r"-k^{o}", r" & 0 \end{pmatrix}",
            r"\begin{pmatrix} \Delta_{1} \\ \Delta_{2} \end{pmatrix}"
        ).scale(1.5)
        
        matrix_eq[2].set_color(GREEN) # +k^o
        matrix_eq[4].set_color(RED)   # -k^o
        
        matrix_eq[2].set_color(GREEN) # +k^o
        matrix_eq[4].set_color(RED)   # -k^o
        
        self.play(Write(matrix_eq))
        self.wait(3)
        
        # Clear screen for Part 2
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        # ==========================================================
        # PART 2: BUILDING THE NET FORCE
        # ==========================================================
        
        node = Dot(ORIGIN, color=WHITE, radius=0.3)
        node_label = Text("Mass (m)", font_size=24).next_to(node, DOWN)
        
        self.play(FadeIn(node, node_label))
        
        # Force 1: Passive
        vec_passive = Arrow(ORIGIN, LEFT * 1.5, color=BLUE, buff=0.4)
        eq_passive = MathTex(r"F_{passive} = k^{e}\delta_i", color=BLUE).to_corner(UL)
        
        self.play(GrowArrow(vec_passive), Write(eq_passive))
        self.wait(1)
        
        # Force 2: Active
        vec_active = Arrow(ORIGIN, RIGHT * 3.0, color=ORANGE, buff=0.4)
        eq_active = MathTex(r"F_{active} = k^{o}(\delta_{i+1} - \delta_{i-1})", color=ORANGE).next_to(eq_passive, DOWN, aligned_edge=LEFT)
        
        self.play(GrowArrow(vec_active), Write(eq_active))
        self.wait(1)
        
        # Force 3: Viscous
        vec_viscous = Arrow(ORIGIN, LEFT * 1.0, color=GRAY, buff=0.4).shift(UP*0.2)
        eq_viscous = MathTex(r"F_{viscous} = \eta\dot{\delta}_i", color=GRAY).next_to(eq_active, DOWN, aligned_edge=LEFT)
        
        self.play(GrowArrow(vec_viscous), Write(eq_viscous))
        self.wait(1)
        
        # Combine into F = ma
        eom = MathTex(r"\sum F = m a", font_size=60).to_corner(UR)
        eom[0][3].set_color(YELLOW) 
        
        self.play(Write(eom))
        self.play(
            node.animate.set_color(YELLOW),
            FadeOut(vec_passive, vec_active, vec_viscous)
        )
        self.wait(2)
        
        # Clear screen for Part 3
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # ==========================================================
        # PART 3: THE TIME LOOP
        # ==========================================================
        
        title = Text("Time Integration Loop", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        step1 = MathTex(r"1.\text{ Calculate } ", r"a_t = \frac{F_t}{m}")
        step2 = MathTex(r"2.\text{ Update Velocity } ", r"v_{t+1} = v_t + a_t \Delta t")
        step3 = MathTex(r"3.\text{ Update Position } ", r"x_{t+1} = x_t + v_t \Delta t")
        
        loop_group = VGroup(step1, step2, step3).arrange(DOWN, buff=1.2).shift(LEFT * 1)
        
        step1[1][0:2].set_color(YELLOW) 
        step2[1][0:4].set_color(GREEN)  
        step3[1][0:4].set_color(BLUE)   
        
        self.play(Write(step1))
        self.wait(1)
        
        self.play(Write(step2))
        arrow1 = CurvedArrow(step1[1][0:2].get_bottom(), step2[1][7:9].get_top(), angle=-PI/4, color=YELLOW)
        self.play(Create(arrow1))
        self.wait(1)
        
        self.play(Write(step3))
        arrow2 = CurvedArrow(step2[1][0:4].get_bottom(), step3[1][7:9].get_top(), angle=-PI/4, color=GREEN)
        self.play(Create(arrow2))
        self.wait(1)
        
 # Clear screen for the last part
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # 1. Define the main title
        simexplain = Text("Now for the simulations", font_size=40, color=BLUE).to_edge(UP, buff=1.0) # Adjusted buffer so it isn't too far down

        # 2. Anchor the first description to the title
        description_text = Text(
            "The diagonals in the following simulations are non-reciprocal,",
            font_size=24, 
            color=WHITE
        ).next_to(simexplain, DOWN, buff=0.5)

        # 3. Anchor the second description to the FIRST description
        description_textb = Text(
            "while the edges are still reciprocal.",
            font_size=24, 
            color=WHITE
        ).next_to(description_text, DOWN, buff=0.2) # Removed the trailing comma here!

        # 4. Anchor the third description to the SECOND description
        description_textc = Text(
            "We use an offset to start the motion.", 
            font_size=24, 
            color=WHITE
        ).next_to(description_textb, DOWN, buff=0.2)
        
        self.play(Write(simexplain))
        self.play(FadeIn(description_text, shift=UP*0.2))
        self.play(FadeIn(description_textb, shift=UP*0.2))
        self.play(FadeIn(description_textc, shift=UP*0.2))
        self.wait(3)