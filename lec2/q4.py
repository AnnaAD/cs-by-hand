import random
import svgwrite
from svg_logic import draw_and, draw_xor,draw_or,draw_wire







class PrimaryInput:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Gate:
    def __init__(self, gid, gtype, x, y, negate=False):
        self.id = gid
        self.type = gtype      # "and", "or", "xor", "buf"
        self.x = x
        self.y = y
        self.negate = negate
        self.inputs = []       # list of source gate IDs
        self.output = f"G{gid}"

class Wire:
    def __init__(self, src_gate, dst_gate, dst_input_index):
        self.src = src_gate
        self.dst = dst_gate
        self.dst_index = dst_input_index


class Circuit:
    def __init__(self):
        self.gates = {}
        self.wires = []
        self.primary_inputs = []


def draw_gate(dwg, gate):
    #input_labels = [f"G{i}" for i in gate.inputs]
    input_labels = []
    if gate.type == "and":
        draw_and(dwg, gate.x, gate.y, input_labels, gate.output, gate.negate)
    elif gate.type == "or":
        draw_or(dwg, gate.x, gate.y, input_labels, gate.output, gate.negate)
    elif gate.type == "xor":
        draw_xor(dwg, gate.x, gate.y, input_labels, gate.output, gate.negate)

def random_circuit(num_gates=6):
    circuit = Circuit()
    gate_types = ["and", "or", "xor"]

    spacing_x = 120
    spacing_y = 60

    # Create gates
    last = -1
    for i in range(num_gates):
        gtype = random.choice(gate_types)
        x = 120 + i * spacing_x
        y_off = random.randint(0, 3)
        while y_off == last:
            y_off = random.randint(0, 3)
        y = 50 + y_off * spacing_y
        last = y_off
        negate = random.random() < 0.25
        circuit.gates[i] = Gate(i, gtype, x, y, negate)

    # Create gate-to-gate wires
    available_sources = set()
    for i in range(num_gates):
        gate = circuit.gates[i]
        required_inputs = 2 if gate.type != "buf" else 1
        available = list(range(max(0,i-2),i))

        num_connected = min(required_inputs, len(available))
        sources = random.sample(available, num_connected)
        print(sources)

        for idx, src in enumerate(sources):
            gate.inputs.append(src)
            circuit.wires.append(Wire(src, i, idx))
        
        available_sources.add(i)

    # Fill missing inputs with primary inputs
    next_letter = ord("A")

    for gid, gate in circuit.gates.items():
        required_inputs = 2 if gate.type != "buf" else 1
        missing = required_inputs - len(gate.inputs)

        for _ in range(missing):
            name = chr(next_letter)
            next_letter += 1

            y = gate.y + 10 + len(gate.inputs) * 20
            pi = PrimaryInput(name, 30, y)
            circuit.primary_inputs.append(pi)

            # fake a wire from primary input to this gate
            circuit.wires.append(Wire(name, gid, len(gate.inputs)))
            gate.inputs.append(name)

    return circuit



# ------------- Circuit Renderer -------------

def draw_circuit(dwg):
    circuit = random_circuit(6)

    from collections import defaultdict

    # Count how many wires leave each source
    fanout = defaultdict(int)
    for wire in circuit.wires:
        fanout[wire.src] += 1

    # Draw gates
    for gate in circuit.gates.values():
        draw_gate(dwg, gate)

    for wire in circuit.wires:
        dst_gate = circuit.gates[wire.dst]
        dst_in = (dst_gate.x, dst_gate.y + 10 + wire.dst_index * 20)

        # Source
        if isinstance(wire.src, int):
            src_gate = circuit.gates[wire.src]
            src_out = (src_gate.x + 50, src_gate.y + 20)
        else:
            # Primary input
            pi = next(p for p in circuit.primary_inputs if p.name == wire.src)
            src_out = (pi.x + 20, pi.y)

            # Draw label
            dwg.add(dwg.text(
                pi.name,
                insert=(pi.x - 10, pi.y + 5),
                text_anchor="middle",
                font_size=14
            ))

        draw_dot = fanout[wire.src] > 1
        fanout[wire.src]-=1
        draw_wire(dwg, src_out, dst_in, draw_dot=draw_dot)

def draw_timing_table(dwg,x,y,row_height, col_width, inputs):

    row_headers = ["Gate","Tpd", "Tcd"]

    width = len(row_headers)*col_width
    height = len(inputs[0])*row_height

    dwg.add(dwg.rect(
            insert=(x, y),
            size=(width, height),
            fill="none",
            stroke="black"
    ))

    for i in range(len(row_headers)):
        tx = x + i * col_width
        dwg.add(dwg.text(
            f"{row_headers[i]}",
            insert=(tx + col_width/2, y),
            text_anchor="middle",
            font_size=14
        ))
        dwg.add(dwg.line(start=(tx+col_width,y),
            end=(tx+col_width,y+height),
            stroke="black",
            stroke_width=2 if i == len(inputs)-1 else 1))

    for i in range(len(inputs[0])):
        ty = y + i*row_height
        dwg.add(dwg.line(start=(x,ty),
            end=(x+width,ty),
            stroke="black",
            stroke_width=1))
    
    for j in range(len(inputs[0])):
        ty = y + j*row_height
        for i in range(len(inputs)):
            tx = x + i * col_width
            dwg.add(dwg.text(
                inputs[i][j],
                insert=(tx + col_width/2, ty + row_height/2),
                text_anchor="middle",
                font_size=14
            ))


if __name__ == "__main__":
    width = 850
    height = 600
    margin = 20
    dwg = svgwrite.Drawing("outputs/lec2/q4.svg", size=(width, height))
    draw_circuit(dwg)

    gate_types = ["and", "or", "xor", "nand","nor","notxor"]

    inputs = [[],[],[]]
    for g in gate_types:
        inputs[0].append(g)
        inputs[1].append(random.randint(20,50))
        inputs[2].append(random.randint(1,20))

    draw_timing_table(dwg, width/2 - 1.5*50, 300, 30,50,inputs)

    dwg.add(dwg.text(
        f"What is the Tpd and Tcd of the above circuit?",
        insert=(width/2, 300 + margin + 30*len(inputs[0])),
        text_anchor="middle",
        font_size=14
    ))

    dwg.save()

