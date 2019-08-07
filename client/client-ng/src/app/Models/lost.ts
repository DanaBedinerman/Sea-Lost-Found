import { Point } from './point';

export class Lost {
    constructor(
        public id: string,
        public location: Point,
        public radius: number,
        public vector: number,
    ) { }
}
