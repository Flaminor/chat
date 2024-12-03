{pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	buildInputs = [
		pkgs.git
		pkgs.python313Full
		pkgs.vim	
		];
}
