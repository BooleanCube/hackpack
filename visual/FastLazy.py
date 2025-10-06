from manim import *

class StorageAndIndexing(Scene):
    """Section 1: Storage and Indexing"""
    def construct(self):
        # Title
        section_title = Tex(r"\textbf{Storage and Indexing}", font_size=44)
        section_title.to_edge(UP, buff=0.3)
        self.play(Write(section_title))
        self.wait()
        
        # Example with n=8
        n = 8
        
        # Show the array representation at the top
        array_label = Tex(r"Array with $n=8$ elements:", font_size=24)
        array_label.next_to(section_title, DOWN, buff=0.3)
        self.play(Write(array_label))
        
        # Create array visualization - smaller and at the top
        array_boxes = VGroup()
        array_values = VGroup()
        for i in range(n):
            box = Square(side_length=0.4)
            box.shift(RIGHT * (i - n/2 + 0.5) * 0.5)
            box.shift(UP * 2.2)
            array_boxes.add(box)
            
            idx = Tex(str(i), font_size=16)
            idx.move_to(box)
            array_values.add(idx)
        
        self.play(FadeIn(array_boxes), Write(array_values))
        self.wait()
        
        # Show tree structure label in the middle
        tree_label = Tex(r"Tree structure: $2n$ nodes, indices $1$ to $2n-1$", font_size=22)
        tree_label.move_to(UP * 1.3)
        self.play(Write(tree_label))
        
        # Create tree nodes with proper edges - positioned lower
        tree_nodes, node_positions = self.create_tree_visual(n, start_y=0.5)
        self.play(FadeIn(tree_nodes), run_time=1.5)
        self.wait()
        
        # Highlight root at the bottom
        index_text = Tex(r"Root at index $1$", font_size=22, color=YELLOW)
        index_text.to_edge(DOWN, buff=0.5)
        self.play(
            node_positions[1][0].animate.set_stroke(color=YELLOW, width=3),
            node_positions[1][1].animate.set_color(YELLOW),
            Write(index_text)
        )
        self.wait(1)
        
        # Show parent-child relationship - Example 1: Node 1
        index_text2 = Tex(r"Node $1$: left child $= 2 \times 1 = 2$ (even), right child $= 2 \times 1 + 1 = 3$ (odd)", 
                         font_size=18, color=GREEN)
        index_text2.to_edge(DOWN, buff=0.5)
        
        # Highlight node 2 (left, even) and 3 (right, odd) as children of 1
        self.play(
            node_positions[2][0].animate.set_stroke(color=GREEN, width=3),
            node_positions[2][1].animate.set_color(GREEN),
            node_positions[3][0].animate.set_stroke(color=ORANGE, width=3),
            node_positions[3][1].animate.set_color(ORANGE),
            Transform(index_text, index_text2)
        )
        self.wait(2.5)
        
        # Reset colors for node 1, 2, 3
        self.play(
            node_positions[1][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[1][1].animate.set_color(WHITE),
            node_positions[2][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[2][1].animate.set_color(WHITE),
            node_positions[3][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[3][1].animate.set_color(WHITE),
        )
        
        # Example 2: Node 2
        index_text3 = Tex(r"Node $2$: left child $= 2 \times 2 = 4$ (even), right child $= 2 \times 2 + 1 = 5$ (odd)", 
                         font_size=18, color=GREEN)
        index_text3.to_edge(DOWN, buff=0.5)
        
        self.play(
            node_positions[2][0].animate.set_stroke(color=YELLOW, width=3),
            node_positions[2][1].animate.set_color(YELLOW),
            node_positions[4][0].animate.set_stroke(color=GREEN, width=3),
            node_positions[4][1].animate.set_color(GREEN),
            node_positions[5][0].animate.set_stroke(color=ORANGE, width=3),
            node_positions[5][1].animate.set_color(ORANGE),
            Transform(index_text, index_text3)
        )
        self.wait(2.5)
        
        # Reset colors
        self.play(
            node_positions[2][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[2][1].animate.set_color(WHITE),
            node_positions[4][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[4][1].animate.set_color(WHITE),
            node_positions[5][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[5][1].animate.set_color(WHITE),
        )
        
        # Example 3: Node 3
        index_text4 = Tex(r"Node $3$: left child $= 2 \times 3 = 6$ (even), right child $= 2 \times 3 + 1 = 7$ (odd)", 
                         font_size=18, color=GREEN)
        index_text4.to_edge(DOWN, buff=0.5)
        
        self.play(
            node_positions[3][0].animate.set_stroke(color=YELLOW, width=3),
            node_positions[3][1].animate.set_color(YELLOW),
            node_positions[6][0].animate.set_stroke(color=GREEN, width=3),
            node_positions[6][1].animate.set_color(GREEN),
            node_positions[7][0].animate.set_stroke(color=ORANGE, width=3),
            node_positions[7][1].animate.set_color(ORANGE),
            Transform(index_text, index_text4)
        )
        self.wait(2.5)
        
        # Reset colors
        self.play(
            node_positions[3][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[3][1].animate.set_color(WHITE),
            node_positions[6][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[6][1].animate.set_color(WHITE),
            node_positions[7][0].animate.set_stroke(color=WHITE, width=2),
            node_positions[7][1].animate.set_color(WHITE),
        )
        
        # Show general rule emphasizing parity
        index_text5 = Tex(r"Rule: Left child (even index), Right child (odd index)", 
                         font_size=20, color=PURPLE)
        index_text5.to_edge(DOWN, buff=0.5)
        self.play(Transform(index_text, index_text5))
        self.wait(2)
        
        # Show parent formula
        index_text6 = Tex(r"Parent of any node: $\lfloor \text{idx}/2 \rfloor$ (both children point to same parent)", 
                         font_size=18, color=PURPLE)
        index_text6.to_edge(DOWN, buff=0.5)
        self.play(Transform(index_text, index_text6))
        self.wait(2)
        
        # Show leaf nodes mapping
        index_text3 = Tex(r"Leaves (indices $n$ to $2n-1$) map to array", font_size=20, color=BLUE)
        index_text3.to_edge(DOWN, buff=0.5)
        
        leaf_anims = []
        for i in range(n, 2*n):
            leaf_anims.extend([
                node_positions[i][0].animate.set_stroke(color=BLUE, width=3),
                node_positions[i][1].animate.set_color(BLUE)
            ])
        
        self.play(*leaf_anims, Transform(index_text, index_text3))
        self.wait()
        
        # Show specific mapping with arrows
        index_text4 = Tex(r"Index $n+i$ stores array element $i$", font_size=20, color=BLUE)
        index_text4.to_edge(DOWN, buff=0.5)
        
        # Draw arrows from a few leaf nodes to array positions
        arrows = VGroup()
        for i in [0, 3, 7]:
            arrow = Arrow(
                node_positions[n+i].get_top(),
                array_boxes[i].get_bottom(),
                buff=0.05,
                stroke_width=2,
                color=BLUE,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)
        
        self.play(
            *[Create(arrow) for arrow in arrows],
            Transform(index_text, index_text4)
        )
        self.wait(3)

    def create_tree_visual(self, n, start_y=0):
        """Create visual representation of tree nodes with proper edges"""
        all_objects = VGroup()
        node_positions = {}
        node_positions[0] = VMobject()  # Placeholder for index 0
        
        # First pass: calculate all positions - make tree more compact
        positions = {}
        for idx in range(1, 2*n):
            level = int(np.log2(idx)) if idx > 0 else 0
            level_start = 2**level
            pos_in_level = idx - level_start
            num_in_level = 2**level
            
            # Position - tighter vertical spacing
            y = start_y - level * 0.7
            x_spacing = 5.5 / num_in_level
            x = (pos_in_level - num_in_level/2 + 0.5) * x_spacing
            positions[idx] = np.array([x, y, 0])
        
        # Second pass: draw edges first
        edges = VGroup()
        for idx in range(2, 2*n):
            parent_idx = idx // 2
            if parent_idx >= 1:
                edge = Line(
                    positions[parent_idx],
                    positions[idx],
                    stroke_width=1.5,
                    color=WHITE
                )
                edges.add(edge)
        
        all_objects.add(edges)
        
        # Third pass: draw nodes on top - smaller nodes
        for idx in range(1, 2*n):
            circle = Circle(radius=0.2, color=WHITE, fill_opacity=1, fill_color=BLACK)
            label = Tex(str(idx), font_size=14)
            label.move_to(circle)
            node = VGroup(circle, label)
            node.move_to(positions[idx])
            
            all_objects.add(node)
            node_positions[idx] = node
        
        return all_objects, node_positions


class Construction(Scene):
    """Section 2: Construction and Range Storage"""
    def construct(self):
        section_title = Tex(r"\textbf{Construction: Range Storage}", font_size=48)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        self.wait()
        
        n = 4  # Smaller tree for clarity
        
        # Explain the purpose - position in center between title and tree
        explanation = Tex(r"Each node stores its range $[L, R]$", font_size=32)
        explanation.next_to(section_title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait()
        
        # Create tree with range labels
        tree_data, node_positions = self.create_tree_with_ranges(n, start_y=-0.5)
        self.play(FadeIn(tree_data), run_time=1)
        self.wait()
        
        # Show construction process - position text in the center space
        construction_text = Tex(r"\textbf{Recursive construction:}", font_size=28)
        construction_text.next_to(explanation, DOWN, buff=0.3)
        self.play(Write(construction_text))
        
        # Animate construction from leaves up
        steps = [
            (r"Leaves: $[i, i]$ for each element", [(4, BLUE), (5, BLUE), (6, BLUE), (7, BLUE)]),
            (r"Internal: $[\text{left}.L, \text{right}.R]$", [(2, GREEN), (3, GREEN)]),
            (r"Root: $[0, n-1]$", [(1, YELLOW)])
        ]
        
        for step_text, nodes_to_highlight in steps:
            step = Tex(step_text, font_size=26)
            step.next_to(construction_text, DOWN, buff=0.3)
            self.play(Write(step))
            
            for idx, color in nodes_to_highlight:
                # Change only the rectangle border color, not fill
                node_rect = node_positions[idx][0]  # Get the rectangle
                node_text = node_positions[idx][1]  # Get the text
                self.play(
                    node_rect.animate.set_stroke(color=color, width=3),
                    node_text.animate.set_color(color)
                )
            self.wait(1.5)
            self.play(FadeOut(step))
        
        # Fade out construction text before showing formula
        self.play(FadeOut(construction_text))
        
        # Show the formula in the center
        formula = Tex(r"\text{Node Range Length} = R - L + 1", font_size=28, color=ORANGE)
        formula.next_to(explanation, DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(3)

    def create_tree_with_ranges(self, n, start_y=0):
        """Create tree with range labels and edges"""
        all_objects = VGroup()
        node_positions = {}
        node_positions[0] = VMobject()  # Placeholder for index 0
        
        # Calculate ranges
        ranges = {1: [0, n-1]}
        for idx in range(1, n):
            mid = (ranges[idx][0] + ranges[idx][1]) // 2
            ranges[2*idx] = [ranges[idx][0], mid]
            ranges[2*idx + 1] = [mid + 1, ranges[idx][1]]
        for idx in range(n, 2*n):
            ranges[idx] = [idx - n, idx - n]
        
        # First pass: create nodes and store positions
        positions = {}
        for idx in range(1, 2*n):
            level = int(np.log2(idx)) if idx > 0 else 0
            level_start = 2**level
            pos_in_level = idx - level_start
            num_in_level = 2**level
            
            # Position
            y = start_y - level * 1.2
            x_spacing = 7 / num_in_level
            x = (pos_in_level - num_in_level/2 + 0.5) * x_spacing
            positions[idx] = np.array([x, y, 0])
        
        # Second pass: draw edges first
        edges = VGroup()
        for idx in range(2, 2*n):
            parent_idx = idx // 2
            if parent_idx >= 1:
                edge = Line(
                    positions[parent_idx],
                    positions[idx],
                    stroke_width=2,
                    color=WHITE
                )
                edges.add(edge)
        
        all_objects.add(edges)
        
        # Third pass: draw nodes on top of edges
        for idx in range(1, 2*n):
            # Create node with range
            rect = Rectangle(width=1, height=0.5, color=WHITE, fill_opacity=1, fill_color=BLACK)
            if idx in ranges:
                range_text = Tex(f"[{ranges[idx][0]},{ranges[idx][1]}]", font_size=18)
            else:
                range_text = Tex(r"[?,?]", font_size=18)
            range_text.move_to(rect)
            node = VGroup(rect, range_text)
            node.move_to(positions[idx])
            
            all_objects.add(node)
            node_positions[idx] = node
        
        return all_objects, node_positions


class RangeUpdate(Scene):
    """Section 3: Range Update"""
    def construct(self):
        section_title = Tex(r"\textbf{Range Update:} Add value to $[L, R]$", font_size=44)
        section_title.to_edge(UP, buff=0.2)
        self.play(Write(section_title))
        self.wait()
        
        n = 8
        
        # Show the operation - using range [1, 6] for more interesting coverage
        operation = Tex(r"\texttt{update}(1, 6, +5)", font_size=32, color=YELLOW)
        operation.next_to(section_title, DOWN, buff=0.2)
        self.play(Write(operation))
        self.wait()
        
        # Create tree with proper structure and range labels - shifted up
        tree_data, node_positions, ranges = self.create_tree_with_ranges(n, start_y=2.0)
        self.play(FadeIn(tree_data), run_time=1)
        self.wait()
        
        # Show array representation at bottom - moved higher to avoid overlap
        array_boxes = self.create_array_boxes(n, y_pos=-3.0)
        array_labels = VGroup()
        for i in range(n):
            label = Tex(str(i), font_size=18)
            label.next_to(array_boxes[i], DOWN, buff=0.1)
            array_labels.add(label)
        
        self.play(Create(array_boxes), Write(array_labels))
        
        # Highlight update range in array [1, 6]
        update_highlights = VGroup(*[array_boxes[i] for i in range(1, 7)])
        self.play(update_highlights.animate.set_fill(YELLOW, opacity=0.3))
        self.wait()
        
        # Animate finding minimal covering set using bottom-up approach
        # Place text centered between tree and array - moved higher
        explanation = Tex(r"Find minimal node cover: bottom-up approach", font_size=24)
        explanation.shift(DOWN * 1.0)
        self.play(Write(explanation))
        self.wait()
        
        # Start with leaf boundaries: l = 1+n = 9, r = 6+n = 14
        l_idx = 1 + n  # 9
        r_idx = 6 + n  # 14
        
        boundary_text = Tex(f"Current Range: $l = {l_idx}$ (array[1]), $r = {r_idx}$ (array[6])", font_size=22, color=BLUE)
        boundary_text.next_to(explanation, DOWN, buff=0.2)
        self.play(Write(boundary_text))
        
        # Highlight the boundaries
        for idx in [l_idx, r_idx]:
            circle = node_positions[idx][0]
            label = node_positions[idx][1]
            self.play(
                circle.animate.set_stroke(color=BLUE, width=3),
                label.animate.set_color(BLUE),
                run_time=0.4
            )
        self.wait(1)
        
        covering_nodes = []
        iteration = 0
        
        # Status text that persists
        status_text = Tex("", font_size=20)
        status_text.next_to(boundary_text, DOWN, buff=0.2)
        
        # Simulate the loop: while l < r
        while l_idx < r_idx:
            iteration += 1
            
            # Check if l is odd (right child)
            if l_idx & 1:
                new_status = Tex(f"Iter {iteration}: $l={l_idx}$ is odd (right child) → include it", 
                               font_size=20, color=GREEN)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                
                # Mark this node as part of covering set
                circle = node_positions[l_idx][0]
                label = node_positions[l_idx][1]
                self.play(
                    circle.animate.set_stroke(color=GREEN, width=3),
                    label.animate.set_color(GREEN),
                    run_time=0.4
                )
                covering_nodes.append(l_idx)
                
                # Show l++ update
                old_l = l_idx
                l_idx += 1
                update_l_text = Tex(f"$l$ becomes ${l_idx}$ (was ${old_l}$)", 
                                   font_size=18, color=BLUE)
                update_l_text.next_to(status_text, DOWN, buff=0.15)
                self.play(Write(update_l_text))

                new_boundary = Tex(f"Current Range: $l = {l_idx}$, $r = {r_idx}$", font_size=22, color=BLUE)
                new_boundary.next_to(explanation, DOWN, buff=0.2)
                self.play(Transform(boundary_text, new_boundary))

                
                # Update visual highlight
                old_circle = node_positions[old_l][0]
                old_label = node_positions[old_l][1]
                self.play(
                    old_circle.animate.set_stroke(color=GREEN, width=3),
                    old_label.animate.set_color(GREEN),
                    run_time=0.2
                )
                if l_idx <= 2*n-1 and l_idx not in covering_nodes:
                    circle = node_positions[l_idx][0]
                    label = node_positions[l_idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
                
                self.wait(0.8)
                self.play(FadeOut(update_l_text))
            else:
                new_status = Tex(f"Iter {iteration}: $l={l_idx}$ is even (left child) → skip", 
                               font_size=20, color=GRAY)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                self.wait(0.6)
            
            # Check if l == r (break condition)
            if l_idx == r_idx:
                break_status = Tex(f"$l = r = {l_idx}$ → exit loop", font_size=20, color=RED)
                break_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, break_status))
                self.wait(1)
                break
            
            # Check if r is even (left child)
            if not (r_idx & 1):
                new_status = Tex(f"Iter {iteration}: $r={r_idx}$ is even (left child) → include it", 
                               font_size=20, color=GREEN)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                
                # Mark this node as part of covering set
                circle = node_positions[r_idx][0]
                label = node_positions[r_idx][1]
                self.play(
                    circle.animate.set_stroke(color=GREEN, width=3),
                    label.animate.set_color(GREEN),
                    run_time=0.4
                )
                covering_nodes.append(r_idx)
                
                # Show r-- update
                old_r = r_idx
                r_idx -= 1
                update_r_text = Tex(f"$r$ becomes ${r_idx}$ (was ${old_r}$)", 
                                   font_size=18, color=BLUE)
                update_r_text.next_to(status_text, DOWN, buff=0.15)
                self.play(Write(update_r_text))

                new_boundary = Tex(f"Current Range: $l = {l_idx}$, $r = {r_idx}$", font_size=22, color=BLUE)
                new_boundary.next_to(explanation, DOWN, buff=0.2)
                self.play(Transform(boundary_text, new_boundary))
                
                # Update visual highlight
                old_circle = node_positions[old_r][0]
                old_label = node_positions[old_r][1]
                self.play(
                    old_circle.animate.set_stroke(color=GREEN, width=3),
                    old_label.animate.set_color(GREEN),
                    run_time=0.2
                )
                if r_idx >= 1 and r_idx not in covering_nodes:
                    circle = node_positions[r_idx][0]
                    label = node_positions[r_idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
                
                self.wait(0.8)
                self.play(FadeOut(update_r_text))
            else:
                new_status = Tex(f"Iter {iteration}: $r={r_idx}$ is odd (right child) → skip", 
                               font_size=20, color=GRAY)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                self.wait(0.6)
            
            # Move up: l >>= 1, r >>= 1
            old_l = l_idx
            old_r = r_idx
            new_l = l_idx >> 1
            new_r = r_idx >> 1
            
            move_status = Tex(f"Move up tree: $l = {new_l}$, $r = {new_r}$", 
                          font_size=20, color=PURPLE)
            move_status.next_to(boundary_text, DOWN, buff=0.2)
            self.play(Transform(status_text, move_status))

            new_boundary = Tex(f"Current Range: $l = {l_idx}$, $r = {r_idx}$", font_size=22, color=BLUE)
            new_boundary.next_to(explanation, DOWN, buff=0.2)
            self.play(Transform(boundary_text, new_boundary))
            
            # Reset blue highlights on old boundaries
            for idx in [old_l, old_r]:
                if idx not in covering_nodes and idx >= 1 and idx <= 2*n-1:
                    circle = node_positions[idx][0]
                    label = node_positions[idx][1]
                    self.play(
                        circle.animate.set_stroke(color=WHITE, width=2),
                        label.animate.set_color(WHITE),
                        run_time=0.15
                    )
            
            l_idx = new_l
            r_idx = new_r
            
            # Highlight new boundaries
            for idx in [l_idx, r_idx]:
                if idx not in covering_nodes and idx >= 1:
                    circle = node_positions[idx][0]
                    label = node_positions[idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
            
            self.wait(0.8)
        
        # Final node (when l == r)
        final_status = Tex(f"Final: include node ${l_idx}$", font_size=20, color=GREEN)
        final_status.next_to(boundary_text, DOWN, buff=0.2)
        self.play(Transform(status_text, final_status))
        
        circle = node_positions[l_idx][0]
        label = node_positions[l_idx][1]
        self.play(
            circle.animate.set_stroke(color=GREEN, width=3),
            label.animate.set_color(GREEN),
            run_time=0.4
        )
        covering_nodes.append(l_idx)
        self.wait(1)
        
        self.play(FadeOut(status_text), FadeOut(boundary_text))
        
        # Update explanation
        found_text = Tex(f"Covering set: nodes {', '.join(map(str, covering_nodes))}", 
                        font_size=22, color=GREEN)
        found_text.shift(DOWN * 1.8)
        self.play(Transform(explanation, found_text))
        self.wait(1.5)
        
        # Show lazy propagation concept
        lazy_text = Tex(r"Mark each: $\text{lazy}[\text{node}] += 5$ (per element)", 
                       font_size=20, color=PURPLE)
        lazy_text.shift(DOWN * 1.0)
        self.play(Transform(explanation, lazy_text))
        self.wait(1.5)
        
        # Now update ancestors for EACH covering node with correct contribution
        ancestor_text = Tex(r"Updating ancestors with contributions...", 
                           font_size=20, color=ORANGE)
        ancestor_text.shift(DOWN * 1.0)
        self.play(Transform(explanation, ancestor_text))
        self.wait()
        
        contrib_text = Tex("", font_size=18)
        contrib_text.next_to(ancestor_text, DOWN, buff=0.15)
        
        # For each covering node, show the ancestor update process
        for node_idx in covering_nodes:
            # Calculate contribution
            node_range = ranges[node_idx]
            range_length = node_range[1] - node_range[0] + 1
            contribution = 5 * range_length
            
            # Show contribution calculation
            new_contrib = Tex(
                f"Node {node_idx} (range [{node_range[0]},{node_range[1]}]): " + 
                f"len={range_length}, add {contribution}",
                font_size=18,
                color=ORANGE
            )
            new_contrib.shift(DOWN * 1.0)
            self.play(Transform(explanation, new_contrib))
            
            # Highlight path to root
            current = node_idx
            path_nodes = []
            while current >= 1:
                path_nodes.append(current)
                current //= 2
            
            # Animate the path
            for path_node in path_nodes:
                circle = node_positions[path_node][0]
                label = node_positions[path_node][1]
                self.play(
                    circle.animate.set_stroke(color=ORANGE, width=3),
                    label.animate.set_color(ORANGE),
                    run_time=0.25
                )
            
            self.wait(0.8)
            
            # Reset path (except the original covering node stays green)
            for path_node in path_nodes:
                if path_node != node_idx:
                    circle = node_positions[path_node][0]
                    label = node_positions[path_node][1]
                    self.play(
                        circle.animate.set_stroke(color=WHITE, width=2),
                        label.animate.set_color(WHITE),
                        run_time=0.15
                    )
        
        # Show final formula
        formula = Tex(
            r"Each ancestor: $\text{tree}[\text{node}] += \text{val} \times \text{length}$", 
            font_size=20, 
            color=RED
        )
        formula.shift(DOWN * 1.0)
        self.play(Transform(explanation, formula))
        self.wait(3)

    def create_tree_with_ranges(self, n, start_y=0):
        """Create visual representation of tree nodes with proper edges and range labels"""
        all_objects = VGroup()
        node_positions = {}
        node_positions[0] = VMobject()  # Placeholder for index 0
        
        # Calculate ranges for all nodes
        ranges = {}
        ranges[1] = [0, n-1]
        for idx in range(1, n):
            mid = (ranges[idx][0] + ranges[idx][1]) // 2
            ranges[2*idx] = [ranges[idx][0], mid]
            ranges[2*idx + 1] = [mid + 1, ranges[idx][1]]
        for idx in range(n, 2*n):
            ranges[idx] = [idx - n, idx - n]
        
        # First pass: calculate all positions
        positions = {}
        for idx in range(1, 2*n):
            level = int(np.log2(idx)) if idx > 0 else 0
            level_start = 2**level
            pos_in_level = idx - level_start
            num_in_level = 2**level
            
            # Position - tighter vertical spacing
            y = start_y - level * 0.75
            x_spacing = 5.5 / num_in_level
            x = (pos_in_level - num_in_level/2 + 0.5) * x_spacing
            positions[idx] = np.array([x, y, 0])
        
        # Second pass: draw edges first
        edges = VGroup()
        for idx in range(2, 2*n):
            parent_idx = idx // 2
            if parent_idx >= 1:
                edge = Line(
                    positions[parent_idx],
                    positions[idx],
                    stroke_width=1.5,
                    color=WHITE
                )
                edges.add(edge)
        
        all_objects.add(edges)
        
        # Third pass: draw nodes on top with range labels
        for idx in range(1, 2*n):
            circle = Circle(radius=0.22, color=WHITE, fill_opacity=1, fill_color=BLACK)
            
            # Node label shows index and range
            node_range = ranges[idx]
            if node_range[0] == node_range[1]:
                label = Tex(f"{idx}$\\atop$[{node_range[0]}]", font_size=10)
            else:
                label = Tex(f"{idx}$\\atop$[{node_range[0]},{node_range[1]}]", font_size=10)
            label.move_to(circle)
            node = VGroup(circle, label)
            node.move_to(positions[idx])
            
            all_objects.add(node)
            node_positions[idx] = node
        
        return all_objects, node_positions, ranges

    def create_array_boxes(self, n, y_pos=-3):
        """Create array visualization"""
        boxes = VGroup()
        for i in range(n):
            box = Square(side_length=0.5)
            box.shift(RIGHT * (i - n/2 + 0.5) * 0.6)
            box.shift(UP * y_pos)
            boxes.add(box)
        return boxes


class RangeQuery(Scene):
    """Section 4: Range Query"""
    def construct(self):
        section_title = Tex(r"\textbf{Range Query:} Sum of $[L, R]$", font_size=44)
        section_title.to_edge(UP, buff=0.2)
        self.play(Write(section_title))
        self.wait()
        
        n = 8
        
        # Show the operation - using range [0, 6]
        operation = Tex(r"\texttt{query}(0, 6)", font_size=32, color=BLUE)
        operation.next_to(section_title, DOWN, buff=0.2)
        self.play(Write(operation))
        self.wait()
        
        # Create tree with proper structure and range labels - shifted up
        tree_data, node_positions, ranges = self.create_tree_with_ranges(n, start_y=2.0)
        self.play(FadeIn(tree_data), run_time=1)
        self.wait()
        
        # Show array representation at bottom
        array_boxes = self.create_array_boxes(n, y_pos=-3.0)
        array_labels = VGroup()
        for i in range(n):
            label = Tex(str(i), font_size=18)
            label.next_to(array_boxes[i], DOWN, buff=0.1)
            array_labels.add(label)
        
        self.play(Create(array_boxes), Write(array_labels))
        
        # Highlight query range in array [0, 6]
        query_highlights = VGroup(*[array_boxes[i] for i in range(0, 7)])
        self.play(query_highlights.animate.set_fill(BLUE, opacity=0.3))
        self.wait()
        
        # Animate finding minimal covering set using bottom-up approach
        explanation = Tex(r"Find minimal node cover: bottom-up approach", font_size=24)
        explanation.shift(DOWN * 1.0)
        self.play(Write(explanation))
        self.wait()
        
        # Start with leaf boundaries: l = 0+n = 8, r = 6+n = 13
        l_idx = 0 + n  # 8
        r_idx = 6 + n  # 13
        
        boundary_text = Tex(f"Current Range: $l = {l_idx}$ (array[0]), $r = {r_idx}$ (array[6])", font_size=22, color=BLUE)
        boundary_text.next_to(explanation, DOWN, buff=0.2)
        self.play(Write(boundary_text))
        
        # Highlight the boundaries
        for idx in [l_idx, r_idx]:
            circle = node_positions[idx][0]
            label = node_positions[idx][1]
            self.play(
                circle.animate.set_stroke(color=BLUE, width=3),
                label.animate.set_color(BLUE),
                run_time=0.4
            )
        self.wait(1)
        
        covering_nodes = []
        iteration = 0
        result_sum = Tex("", font_size=20)
        
        # Status text that persists
        status_text = Tex("", font_size=20)
        status_text.next_to(boundary_text, DOWN, buff=0.2)
        
        # Simulate the loop: while l < r
        while l_idx < r_idx:
            iteration += 1
            
            # Check if l is odd (right child)
            if l_idx & 1:
                new_status = Tex(f"Iter {iteration}: $l={l_idx}$ is odd (right child) → include it", 
                               font_size=20, color=GREEN)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                
                # Mark this node as part of covering set
                circle = node_positions[l_idx][0]
                label = node_positions[l_idx][1]
                self.play(
                    circle.animate.set_stroke(color=GREEN, width=3),
                    label.animate.set_color(GREEN),
                    run_time=0.4
                )
                covering_nodes.append(l_idx)
                
                # Show l++ update
                old_l = l_idx
                l_idx += 1
                update_l_text = Tex(f"$l$ becomes ${l_idx}$ (was ${old_l}$)", 
                                   font_size=18, color=BLUE)
                update_l_text.next_to(status_text, DOWN, buff=0.15)
                self.play(Write(update_l_text))

                new_boundary = Tex(f"Current Range: $l = {l_idx}$, $r = {r_idx}$", font_size=22, color=BLUE)
                new_boundary.next_to(explanation, DOWN, buff=0.2)
                self.play(Transform(boundary_text, new_boundary))
                
                # Update visual highlight
                old_circle = node_positions[old_l][0]
                old_label = node_positions[old_l][1]
                self.play(
                    old_circle.animate.set_stroke(color=GREEN, width=3),
                    old_label.animate.set_color(GREEN),
                    run_time=0.2
                )
                if l_idx <= 2*n-1 and l_idx not in covering_nodes:
                    circle = node_positions[l_idx][0]
                    label = node_positions[l_idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
                
                self.wait(0.8)
                self.play(FadeOut(update_l_text))
            else:
                new_status = Tex(f"Iter {iteration}: $l={l_idx}$ is even (left child) → skip", 
                               font_size=20, color=GRAY)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                self.wait(0.6)
            
            # Check if l == r (break condition)
            if l_idx == r_idx:
                break_status = Tex(f"$l = r = {l_idx}$ → exit loop", font_size=20, color=RED)
                break_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, break_status))
                self.wait(1)
                break
            
            # Check if r is even (left child)
            if not (r_idx & 1):
                new_status = Tex(f"Iter {iteration}: $r={r_idx}$ is even (left child) → include it", 
                               font_size=20, color=GREEN)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                
                # Mark this node as part of covering set
                circle = node_positions[r_idx][0]
                label = node_positions[r_idx][1]
                self.play(
                    circle.animate.set_stroke(color=GREEN, width=3),
                    label.animate.set_color(GREEN),
                    run_time=0.4
                )
                covering_nodes.append(r_idx)
                
                # Show r-- update
                old_r = r_idx
                r_idx -= 1
                update_r_text = Tex(f"$r$ becomes ${r_idx}$ (was ${old_r}$)", 
                                   font_size=18, color=BLUE)
                update_r_text.next_to(status_text, DOWN, buff=0.15)
                self.play(Write(update_r_text))

                new_boundary = Tex(f"Current Range: $l = {l_idx}$, $r = {r_idx}$", font_size=22, color=BLUE)
                new_boundary.next_to(explanation, DOWN, buff=0.2)
                self.play(Transform(boundary_text, new_boundary))
                
                # Update visual highlight
                old_circle = node_positions[old_r][0]
                old_label = node_positions[old_r][1]
                self.play(
                    old_circle.animate.set_stroke(color=GREEN, width=3),
                    old_label.animate.set_color(GREEN),
                    run_time=0.2
                )
                if r_idx >= 1 and r_idx not in covering_nodes:
                    circle = node_positions[r_idx][0]
                    label = node_positions[r_idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
                
                self.wait(0.8)
                self.play(FadeOut(update_r_text))
            else:
                new_status = Tex(f"Iter {iteration}: $r={r_idx}$ is odd (right child) → skip", 
                               font_size=20, color=GRAY)
                new_status.next_to(boundary_text, DOWN, buff=0.2)
                self.play(Transform(status_text, new_status))
                self.wait(0.6)
            
            # Move up: l >>= 1, r >>= 1
            old_l = l_idx
            old_r = r_idx
            new_l = l_idx >> 1
            new_r = r_idx >> 1
            
            move_status = Tex(f"Move up tree: $l = {new_l}$, $r = {new_r}$", 
                          font_size=20, color=PURPLE)
            move_status.next_to(boundary_text, DOWN, buff=0.2)
            self.play(Transform(status_text, move_status))

            new_boundary = Tex(f"Current Range: $l = {new_l}$, $r = {new_r}$", font_size=22, color=BLUE)
            new_boundary.next_to(explanation, DOWN, buff=0.2)
            self.play(Transform(boundary_text, new_boundary))
            
            # Reset blue highlights on old boundaries
            for idx in [old_l, old_r]:
                if idx not in covering_nodes and idx >= 1 and idx <= 2*n-1:
                    circle = node_positions[idx][0]
                    label = node_positions[idx][1]
                    self.play(
                        circle.animate.set_stroke(color=WHITE, width=2),
                        label.animate.set_color(WHITE),
                        run_time=0.15
                    )
            
            l_idx = new_l
            r_idx = new_r
            
            # Highlight new boundaries
            for idx in [l_idx, r_idx]:
                if idx not in covering_nodes and idx >= 1:
                    circle = node_positions[idx][0]
                    label = node_positions[idx][1]
                    self.play(
                        circle.animate.set_stroke(color=BLUE, width=3),
                        label.animate.set_color(BLUE),
                        run_time=0.3
                    )
            
            self.wait(0.8)
        
        # Final node (when l == r)
        final_status = Tex(f"Final: include node ${l_idx}$", font_size=20, color=GREEN)
        final_status.next_to(boundary_text, DOWN, buff=0.2)
        self.play(Transform(status_text, final_status))
        
        circle = node_positions[l_idx][0]
        label = node_positions[l_idx][1]
        self.play(
            circle.animate.set_stroke(color=GREEN, width=3),
            label.animate.set_color(GREEN),
            run_time=0.4
        )
        covering_nodes.append(l_idx)
        self.wait(1)
        
        self.play(FadeOut(status_text), FadeOut(boundary_text))
        
        # Update explanation
        found_text = Tex(f"Covering set: nodes {', '.join(map(str, covering_nodes))}", 
                        font_size=22, color=GREEN)
        found_text.shift(DOWN * 1.8)
        self.play(Transform(explanation, found_text))
        self.wait(1.5)
        
        # Show climbing lazy values for each covering node
        climb_text = Tex(r"For each node: climb ancestors to collect $\text{lazy}$ values", 
                       font_size=20, color=PURPLE)
        climb_text.shift(DOWN * 1.0)
        self.play(Transform(explanation, climb_text))
        self.wait(1.5)
        
        # Process each covering node
        for node_idx in covering_nodes:
            # Calculate contribution
            node_range = ranges[node_idx]
            range_length = node_range[1] - node_range[0] + 1
            
            # Show climbing for this node
            climb_detail = Tex(
                f"Node {node_idx} (range [{node_range[0]},{node_range[1]}]): climb ancestors",
                font_size=18,
                color=PURPLE
            )
            climb_detail.shift(DOWN * 1.0)
            self.play(Transform(explanation, climb_detail))
            
            # Highlight path to root (climbing)
            current = node_idx >> 1  # Start from parent
            path_nodes = []
            while current >= 1:
                path_nodes.append(current)
                current >>= 1
            
            # Animate the climbing path
            for path_node in path_nodes:
                circle = node_positions[path_node][0]
                label = node_positions[path_node][1]
                self.play(
                    circle.animate.set_stroke(color=PURPLE, width=3),
                    label.animate.set_color(PURPLE),
                    run_time=0.25
                )
            
            self.wait(0.8)
            
            # Reset path
            for path_node in path_nodes:
                circle = node_positions[path_node][0]
                label = node_positions[path_node][1]
                self.play(
                    circle.animate.set_stroke(color=WHITE, width=2),
                    label.animate.set_color(WHITE),
                    run_time=0.15
                )
        
        # Show the computation formula
        compute_text = Tex(
            r"$\text{result} = \text{tree}[\text{node}] + \text{climb}(\text{node}) \times \text{length}$", 
            font_size=20, 
            color=ORANGE
        )
        compute_text.shift(DOWN * 1.0)
        self.play(Transform(explanation, compute_text))
        self.wait(1.5)
        
        # Show climb formula
        climb_formula = Tex(
            r"$\text{climb}(\text{idx}) = \sum_{\text{ancestors}} \text{lazy}[\text{anc}]$", 
            font_size=20, 
            color=ORANGE
        )
        climb_formula.shift(DOWN * 1.0)
        self.play(Transform(explanation, climb_formula))
        self.wait(3)

    def create_tree_with_ranges(self, n, start_y=0):
        """Create visual representation of tree nodes with proper edges and range labels"""
        all_objects = VGroup()
        node_positions = {}
        node_positions[0] = VMobject()  # Placeholder for index 0
        
        # Calculate ranges for all nodes
        ranges = {}
        ranges[1] = [0, n-1]
        for idx in range(1, n):
            mid = (ranges[idx][0] + ranges[idx][1]) // 2
            ranges[2*idx] = [ranges[idx][0], mid]
            ranges[2*idx + 1] = [mid + 1, ranges[idx][1]]
        for idx in range(n, 2*n):
            ranges[idx] = [idx - n, idx - n]
        
        # First pass: calculate all positions
        positions = {}
        for idx in range(1, 2*n):
            level = int(np.log2(idx)) if idx > 0 else 0
            level_start = 2**level
            pos_in_level = idx - level_start
            num_in_level = 2**level
            
            # Position - tighter vertical spacing
            y = start_y - level * 0.75
            x_spacing = 5.5 / num_in_level
            x = (pos_in_level - num_in_level/2 + 0.5) * x_spacing
            positions[idx] = np.array([x, y, 0])
        
        # Second pass: draw edges first
        edges = VGroup()
        for idx in range(2, 2*n):
            parent_idx = idx // 2
            if parent_idx >= 1:
                edge = Line(
                    positions[parent_idx],
                    positions[idx],
                    stroke_width=1.5,
                    color=WHITE
                )
                edges.add(edge)
        
        all_objects.add(edges)
        
        # Third pass: draw nodes on top with range labels
        for idx in range(1, 2*n):
            circle = Circle(radius=0.22, color=WHITE, fill_opacity=1, fill_color=BLACK)
            
            # Node label shows index and range
            node_range = ranges[idx]
            if node_range[0] == node_range[1]:
                label = Tex(f"{idx}$\\atop$[{node_range[0]}]", font_size=10)
            else:
                label = Tex(f"{idx}$\\atop$[{node_range[0]},{node_range[1]}]", font_size=10)
            label.move_to(circle)
            node = VGroup(circle, label)
            node.move_to(positions[idx])
            
            all_objects.add(node)
            node_positions[idx] = node
        
        return all_objects, node_positions, ranges

    def create_array_boxes(self, n, y_pos=-3):
        """Create array visualization"""
        boxes = VGroup()
        for i in range(n):
            box = Square(side_length=0.5)
            box.shift(RIGHT * (i - n/2 + 0.5) * 0.6)
            box.shift(UP * y_pos)
            boxes.add(box)
        return boxes


class UsageExamples(Scene):
    """Section 5: Usage Examples"""
    def construct(self):
        section_title = Tex(r"\textbf{Usage Examples}", font_size=48)
        section_title.to_edge(UP)
        self.play(Write(section_title))
        self.wait()
        
        # Show code example
        code_example = Code(
            code_string="""// Create segment tree
segtree<long long> st(8);

// Add 3 to indices [2, 5]
st.update(2, 5, 3);

// Query sum of [0, 7]
auto total = st.query(0, 7);
// Result: 12

// Query sum of [2, 3]
auto partial = st.query(2, 3);
// Result: 6""",
            language="cpp",
            paragraph_config={'font_size': 20},
            background="window",
            add_line_numbers=False
        )
        code_example.scale(0.7)
        code_example.next_to(section_title, DOWN, buff=0.5)
        
        self.play(Create(code_example))
        self.wait(2)
        
        # Show visual result
        n = 8
        array_label = Tex(r"Array state after \texttt{update}(2, 5, 3):", font_size=28)
        array_label.next_to(code_example, DOWN, buff=0.5)
        self.play(Write(array_label))
        
        array_boxes = self.create_array_boxes(n, y_pos=-2.3)
        array_values = VGroup()
        values = [0, 0, 3, 3, 3, 3, 0, 0]
        
        for i in range(n):
            val = Tex(str(values[i]), font_size=28)
            val.move_to(array_boxes[i])
            array_values.add(val)
        
        indices = VGroup()
        for i in range(n):
            idx = Tex(str(i), font_size=18)
            idx.next_to(array_boxes[i], DOWN, buff=0.15)
            indices.add(idx)
        
        self.play(Create(array_boxes), Write(array_values), Write(indices))
        self.wait()
        
        # Highlight query ranges
        range1 = SurroundingRectangle(VGroup(*[array_boxes[i] for i in range(0, 8)]), 
                                      color=YELLOW, buff=0.1)
        label1 = Tex(r"\texttt{query}(0,7) = 12", font_size=24, color=YELLOW)
        label1.next_to(array_boxes, DOWN, buff=0.8)
        
        self.play(Create(range1), Write(label1))
        self.wait(1.5)
        
        self.play(FadeOut(range1), FadeOut(label1))
        
        range2 = SurroundingRectangle(VGroup(*[array_boxes[i] for i in range(2, 4)]), 
                                      color=GREEN, buff=0.1)
        label2 = Tex(r"\texttt{query}(2,3) = 6", font_size=24, color=GREEN)
        label2.next_to(array_boxes, DOWN, buff=0.8)
        
        self.play(Create(range2), Write(label2))
        self.wait(2)
        
        self.play(FadeOut(range2), FadeOut(label2))
        
        # Complexity analysis
        complexity = Tex(r"\textbf{Time Complexity:} $O(\log^2 n)$ per operation", 
                        font_size=28, color=ORANGE)
        complexity.next_to(array_boxes, DOWN, buff=1)
        self.play(Write(complexity))
        self.wait()
        
        space = Tex(r"\textbf{Space Complexity:} $O(n)$", font_size=28, color=ORANGE)
        space.next_to(complexity, DOWN, buff=0.3)
        self.play(Write(space))
        self.wait(3)

    def create_array_boxes(self, n, y_pos=-3):
        """Create array visualization"""
        boxes = VGroup()
        for i in range(n):
            box = Square(side_length=0.6)
            box.shift(RIGHT * (i - n/2 + 0.5) * 0.7)
            box.shift(UP * y_pos)
            boxes.add(box)
        return boxes

