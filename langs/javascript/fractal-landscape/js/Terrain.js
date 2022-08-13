class Terrain {
    constructor (width, height, sections, smoothness) {
        this.width = width;
        this.height = height;
        this.sections = sections;
        this.smoothness = smoothness;
        this.terrain = new Array()

        this.init()
    }

    get array() {
        return this.terrain;
    }

    init() {
        for(let i = 0; i <= this.sections; i++) {
            this.terrain[i] = new Array();
            for(let j = 0; j <= this.sections; j++) {
                this.terrain[i][j] = 0
            }
        }
    }

    generate() {
        let size = this.sections + 1;

        for(let length = this.sections; length >= 2; length /= 2) {
            let half = length / 2;
            this.smoothness /= 2;

            // New Square
            for(let x = 0; x < this.sections; x += length) {
                for(let y = 0; y < this.sections; y += length) {
                    let average = (this.terrain[x][y] +
                                   this.terrain[x+length][y] +
                                   this.terrain[x][y+length] +
                                   this.terrain[x+length][y+length]) / 4;
                    average += 2 * this.smoothness * Math.random() - this.smoothness;
                    this.terrain[x + half][y + half] = average;

                }
            }

            // New Diamond
            for(let x = 0; x < this.sections; x += half) {
                for(let y = (x + half) % length; y < this.sections; y += length) {
                    let average = (this.terrain[(x - half + size) % size][y] +
                                this.terrain[(x + half) % size][y] +
                                this.terrain[x][(y + half) % size] +
                                this.terrain[x][(y - half + size) % size]) / 4;
                    average += 2 * this.smoothness * Math.random() - this.smoothness;
                    this.terrain[x][y] = average;

                    if(x === 0) {
                        this.terrain[this.sections][y] = average;
                    }
                    if(y === 0) {
                        this.terrain[x][this.sections] = average;
                    }
                }
            }
        }
        return this.terrain
    }
}
