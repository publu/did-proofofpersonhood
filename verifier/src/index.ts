import * as dotenv from "dotenv";
import express from "express";
import cors from "cors";
import helmet from "helmet";
import path from "path";
import { router } from "./router";

dotenv.config();

if (!process.env.PORT) {
  process.exit(1);
}

const PORT: number = parseInt((process.env.PORT || 5454) as string, 10);

const app = express();

app.use(helmet());
app.use(cors());
app.use(express.json());

app.set("view engine", "pug");

app.get("/", (req, res) => {
  res.render("index");
});
app.use("/api", router);

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
