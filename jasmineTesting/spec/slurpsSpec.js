describe("Slurps", function () {

	describe("Check to see if scrollToTop equates to the number 0.", function () {
		it("It should be 0.", function () {
			expect(scrollToTop(0)).toBe(0);
		});
		it("It should return an error if not supplied with a number.", function () {
			expect(scrollToTop("Hello World!")).toBe("ERROR!");
		});
	});

	describe("Check to see if scrollBehaviour equates to a string.", function () {
		it("It should be a string.", function () {
			expect(scrollBehaviour("smooth")).toBe("smooth");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(scrollBehaviour(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if windowsScrollTop is more than 300.", function () {
		it("It should be more than 300.", function () {
			expect(windowsScrollTop(500)).toBeGreaterThan(300);
		});
		it("It should return an error if the value is not more than 300.", function () {
			expect(windowsScrollTop(200)).toBe("ERROR!");
		});
	});

	describe("Check to see if stripePublicKeySlices equates to 1 or -1.", function () {
		it("It should be 1 or -1.", function () {
			expect(stripePublicKeySlices(1 | -1)).toBe(1 | -1);
		});
		it("It should return an error if not 1 or -1.", function () {
			expect(stripePublicKeySlices("Hello World!")).toBe("ERROR!");
		});
	});

	describe("Check to see if baseColor equates to a string.", function () {
		it("It should be a string.", function () {
			expect(baseColor("#212529" || "#6c757d")).toBe("#212529" || "#6c757d");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(baseColor(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if baseTextTransform equates to a string.", function () {
		it("It should be a string.", function () {
			expect(baseTextTransform("capitalize")).toBe("capitalize");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(baseTextTransform(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if baseFontFamily equates to a string.", function () {
		it("It should be a string.", function () {
			expect(baseFontFamily("Montserrat, sans-serif")).toBe("Montserrat, sans-serif");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(baseFontFamily(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if baseFontSmoothing equates to a string.", function () {
		it("It should be a string.", function () {
			expect(baseFontSmoothing("antialiased")).toBe("antialiased");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(baseFontSmoothing(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if baseFontSize equates to a string.", function () {
		it("It should be a string.", function () {
			expect(baseFontSize("16px" || "::placeholder")).toBe("16px" || "::placeholder");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(baseFontSize(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if InvalidColor equates to a string.", function () {
		it("It should be a string.", function () {
			expect(InvalidColor("red")).toBe("red");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(InvalidColor(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if formDisabled is a boolean.", function () {
		let formDisabled = true || false;
		it("It should be a boolean.", function () {
			expect(formDisabled).toBe(true || false);
		});
	});

	describe("Check to see if formFadeToggle equates to the number 100.", function () {
		it("It should be 100.", function () {
			expect(formFadeToggle(100)).toBe(100);
		});
		it("It should return an error if not supplied with a number.", function () {
			expect(formFadeToggle("Hello World!")).toBe("ERROR!");
		});
	});

	describe("Check to see if postData equates to a string.", function () {
		it("It should be a string.", function () {
			expect(postData("csrfmiddlewaretoken" || "client_secret" || "save_info")).toBe("csrfmiddlewaretoken" || "client_secret" || "save_info");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(postData(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if url equates to a string.", function () {
		it("It should be a string.", function () {
			expect(url("/payment/cache_payment_data/")).toBe("/payment/cache_payment_data/");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(url(0123)).toBe("ERROR!");
		});
	});

	describe("Check to see if paymentIntentStatus equates to a string.", function () {
		it("It should be a string.", function () {
			expect(paymentIntentStatus("succeeded")).toBe("succeeded");
		});
		it("It should return an error if not supplied with a string.", function () {
			expect(paymentIntentStatus(0123)).toBe("ERROR!");
		});
	});

});