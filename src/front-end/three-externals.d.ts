declare module 'three/examples/jsm/geometries/TextGeometry' {
  import { ExtrudeGeometry } from 'three';
  import { Font } from 'three/examples/jsm/loaders/FontLoader';
  
  export class TextGeometry extends ExtrudeGeometry {
    constructor(text: string, parameters: {
      font: Font;
      size?: number;
      height?: number;
      curveSegments?: number;
      bevelEnabled?: boolean;
      bevelThickness?: number;
      bevelSize?: number;
      bevelOffset?: number;
      bevelSegments?: number;
    });
  }
}

declare module 'three/examples/jsm/loaders/FontLoader' {
  import { Loader } from 'three';

  export class Font {
    data: any;
    constructor(data: any);
  }

  export class FontLoader extends Loader {
    constructor();
    load(
      url: string,
      onLoad?: (font: Font) => void,
      onProgress?: (event: ProgressEvent) => void,
      onError?: (event: ErrorEvent) => void
    ): Font;
    parse(json: any): Font;
  }
}
