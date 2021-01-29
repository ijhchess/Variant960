import chess
import chess.pgn
from pylatex import Document, Section

def toSort(e):
    return e['score']

def main():
    list = []
    pgn = open("unique.pgn", encoding="utf-8-sig")
    for i in range(960):
        game = chess.pgn.read_game(pgn)
        list.append(
        dict(
        id=game.headers["White"].split(" ")[1:][0],
        score=int(game.headers["Black"].split(" ")[1:][0]),
        event=game.headers["Event"],
        line=game.mainline(),
        init_fen=game.board().fen(),
        end_fen=game.end().board().fen()
        )
        )
    list.sort(key=toSort,reverse=True)
    for li in list:
        with open("final.tex", "a") as file_object:
            file_object.write('\section{' +li["event"]+'}\n')
            file_object.write('\\board{'+li["init_fen"]+'}\\bfseries Initial\n')
            file_object.write('\\board{'+li["end_fen"]+'}\\bfseries Final\n')
            file_object.write('\\newline\\variation{'+str(li["line"])+'}\n\n')
main()
