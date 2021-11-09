import './Database'
import express from 'express';
import ways from './routes';

const server = express();
server.use(express.json())
server.use(ways)



server.listen(3213, ()=> console.log('SERVER ON'))