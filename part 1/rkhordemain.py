import asyncio
import chess
import chess.engine
import chess.variant
import chess.pgn

async def main():
    j=0
    file_name="horde960.pgn"
    with open("/path/to/Horde960orRK1440FENS.txt") as f:
        for i in f:
            transport, engine = await chess.engine.popen_uci("/path/to/stockfish.exe")
            board = chess.variant.HordeBoard(i)
            await engine.configure({"Hash": 2048})
            await engine.configure({"Threads": 7})
            info = await engine.analyse(board, chess.engine.Limit(depth=25))
            new_pgn = open(file_name, "a", encoding="utf-8")
            exporter = chess.pgn.FileExporter(new_pgn)
            moves = info["pv"]
            game = chess.pgn.Game()
            game.headers["Event"] = "Position " + str(j).zfill(3) + " Score: " + str(info["score"])
            game.headers["White"] = "Position " + str(j).zfill(3)
            game.headers["Black"] = "Score: " + str(info["score"])
            game.setup(board)
            game.add_line(moves)
            game.accept(exporter)
            print ("position "+str(j).zfill(3)+ " complete")
            j=j+1
            await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())
