import express, { Request, Response } from "express";
import { verify } from "./verifier";
import multer from "multer";

export const router = express.Router();

const upload = multer({ dest: process.env.UPLOAD_FOLDER });

router.post(
  "/validate",
  upload.single("credential"),
  async (req: Request, res: Response) => {
    try {
      const credential = JSON.parse(req.file.buffer.toString());
      res.status(200).send(verify(credential));
    } catch (e) {
      console.log(e);
      res.status(500).send(e);
    }
  }
);
