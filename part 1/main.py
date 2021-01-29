import asyncio
import chess
import chess.engine
import chess.variant
import chess.pgn

async def main():
    j=0
    file_name="n"+str(j).zfill(3)+".pgn"
    for i in range(960):
        j=j+1
        if j == 64:
            j=0
            file_name="n"+str(i).zfill(3)+".pgn"
        transport, engine = await chess.engine.popen_uci("./stockfish")
        board = chess.variant.AtomicBoard().from_chess960_pos(i)
        await engine.configure({"Hash": 2048})
        await engine.configure({"Threads": 4})
        info = await engine.analyse(board, chess.engine.Limit(depth=25))
        new_pgn = open(file_name, "a", encoding="utf-8")
        exporter = chess.pgn.FileExporter(new_pgn)
        moves = info["pv"]
        game = chess.pgn.Game()
        game.headers["Event"] = "Position " + str(i).zfill(3) + " Score: " + str(info["score"])
        game.headers["White"] = "Position " + str(i).zfill(3)
        game.headers["Black"] = "Score: " + str(info["score"])
        game.setup(board)
        game.add_line(moves)
        game.accept(exporter)
        print ("position "+str(i).zfill(3)+ " complete")
        await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())
